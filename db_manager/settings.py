import urllib.parse
from flask import current_app


def get_default_conn_uri():
    default_db_settings = current_app.config['DATABASES']['default']

    default_conn_uri = "postgresql+psycopg://{}:{}@{}/{}".format(
        urllib.parse.quote_plus(default_db_settings['USER']),
        urllib.parse.quote_plus(default_db_settings['PASSWORD']),
        default_db_settings['HOST'], default_db_settings['NAME'])

    return default_conn_uri
