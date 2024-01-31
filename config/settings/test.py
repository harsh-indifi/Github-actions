DEBUG = True
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
CACHE_TYPE = 'redis'
RELAXATION = 10
POOL_SIZE = 1

