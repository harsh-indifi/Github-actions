from flask import Flask
from config.urls import MainBP
import os

from extensions import cache


def create_app():
    app = Flask(__name__)
    flask_env = os.environ.get('FLASK_ENV')
    config_file = f'config.settings.{flask_env}'
    app.config.from_object(config_file)
    # Set config for cache
    cache.init_app(app, config=app.config['CACHES']['default'])
    app.url_map.strict_slashes = False
    app.register_blueprint(MainBP)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
