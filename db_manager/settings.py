import urllib.parse


def get_conn_uri(config):

    default_db_settings = config['DATABASES']['default']
    bs_db_settings = config['DATABASES']['bank_statement']

    default_conn_uri = "postgresql+psycopg://{}:{}@{}/{}".format(
        urllib.parse.quote_plus(default_db_settings['USER']),
        urllib.parse.quote_plus(default_db_settings['PASSWORD']),
        default_db_settings['HOST'], default_db_settings['NAME'])

    bs_db_conn_uri = "postgresql+psycopg://{}:{}@{}/{}".format(
        urllib.parse.quote_plus(bs_db_settings['USER']),
        urllib.parse.quote_plus(bs_db_settings['PASSWORD']),
        bs_db_settings['HOST'], bs_db_settings['NAME'])

    return default_conn_uri, bs_db_conn_uri
