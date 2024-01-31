REDIS_HOST = ''
REDIS_PORT = '6379'

DATABASES = {
    'default': {
        'NAME': 'myTestDb',
        'USER': 'testDbUser',
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

