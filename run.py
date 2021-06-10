from os import environ
from pathlib import Path
from sys import exit


from config.config import app_config_dict
from app import create_app, db

get_config_mode = environ.get('STREAM-101-API_CONFIG_MODE', 'Development')
try:
    config_mode = app_config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Invalid Configuration Mode!')

app = create_app(Path.cwd, config_mode)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)