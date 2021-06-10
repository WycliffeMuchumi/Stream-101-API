from flask import Flask
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from hvac import Client as vaultClient



db = SQLAlchemy(session_options={'expire_on_commit' : False})



"""
    Registering Blueprints
"""

def register_blueprint(app):
    blueprints = (
        'admin',
        'channels',
        'users',
        'videos'
    )

    for blueprint in blueprints:
        module = import_module(f'app.api.{blueprint}')
        app.register_blueprint(module.blueprint)
        print("==> blueprint for {} is registered !".format(blueprint))

"""
    Creting our client vaults
"""
def create_vault_client(app):
    return vaultClient(
        url = app.config.config('VAULT_ADDR'),
        token = app.config.config('VAULT_TOKEN')
    )


"""
    Configuring Database
"""
def configure_database(app):
    @app.before_first_request
    def create_default():
        db.create_all()
       # db.drop_all()

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
    