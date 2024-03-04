REDIS_HOST = ''
REDIS_PORT = '6379'

DATABASES = {
    'default': {
        'NAME': 'mytestdb',
        'USER': 'testdbuser',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'DEPENDENCIES': []
        }
    },
    'bank_statement': {
        'NAME': 'banktestdb',
        'USER': 'testdbuser',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'DEPENDENCIES': []
        }
    },
}

CACHES = {
    "default": {
        "CACHE_TYPE": "RedisCache",
        "CACHE_REDIS_URL": f'redis://{REDIS_HOST}',
        "CACHE_REDIS_OPTIONS": {
            'socket_timeout': 10,
            'socket_connect_timeout': 2,
            'retry_on_timeout': True,
            'max_connections': 20,
        }
    }
}

RELAXATION = 10
POOL_SIZE = 1

SQLALCHEMY_DATABASE_URI = None
SQLALCHEMY_BINDS = {
    'bank_statement_db': None
}
SQLALCHEMY_POOL_CLASS = 'sqlalchemy.pool.QueuePool'
SQLALCHEMY_POOL_SIZE = 1
SQLALCHEMY_POOL_PRE_PING = True
SQLALCHEMY_POOL_RECYCLE = 14400