import os

MODE = os.environ.get('MODE', 'DEV')

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

HASH_MAX_LENGTH = 5

if MODE == 'PROD':
    from conf.prod import *
elif MODE == 'DEV':
    from conf.dev import *
else:
    raise NotImplementedError("mode '%s' not implemented" % MODE)
