from flask import Flask
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from hvac import Client as vaultClient


db = SQLAlchemy(session_options={'expire_on_commit' : False})

"""
    Initializing Bcrypt
"""

bcrypt = Bcrypt()

"""
    Initializing Marshmallow
"""

ma = Marshmallow()


"""
    Registering Blueprints
"""

def register_blueprint(app):
    blueprints = (
        'admin',
        'base',
        'channels',
        'users',
        'videos'
    )

    for blueprint in blueprints:
        module = import_module(f'app.api.{blueprint}')
        app.register_blueprint(module.blueprint)
        print("==> blueprint for {} is registered !".format(blueprint))

"""
    Creating our client vaults
"""

def create_vault_client(app):
    return vaultClient(
        url = app.config.config('VAULT_ADDR'),
        token = app.config.config('VAULT_TOKEN')
    )

from app.api.users.models.users import User
from app.api.users.models.fakedata import fake_data

"""
    Configuring Database
"""

def configure_database(app):
    @app.before_first_request
    def create_default():
        db.create_all()
        # db.drop_all()
        User.metadata.create_all(bind=db.engine)
        # Generating the number of records we want for our fake_data function
        fake_data(100)

"""
    Creating Our Application Factory
"""

def create_app(path, config):
    app = Flask(__name__, static_folder='api/static')
    app.config.from_object(config)
    app.production = not app.config['DEBUG']
    app.path = path
    register_blueprint(app)
    configure_database(app)
    if app.production:
        app.vault_client = create_vault_client(app)
    return app



