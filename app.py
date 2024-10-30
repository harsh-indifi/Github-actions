from flask import Flask
from config.urls import MainBP
import os

from db_manager.settings import get_conn_uri
from extensions import cache, db


def create_app():
    app = Flask(__name__)
    flask_env = os.environ.get('FLASK_ENV')
    config_file = f'config.settings.{flask_env}'
    app.config.from_object(config_file)
    # Set config for cache
    cache.init_app(app, config=app.config['CACHES']['default'])
    app.url_map.strict_slashes = False
    default_uri, bank_statement_uri = get_conn_uri(app.config)
    app.config['SQLALCHEMY_DATABASE_URI'] = default_uri
    app.config['SQLALCHEMY_BINDS']['bank_statement_db'] = bank_statement_uri
    db.init_app(app)
    app.register_blueprint(MainBP)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
