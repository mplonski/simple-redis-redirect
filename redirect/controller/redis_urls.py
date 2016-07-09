from uuid import uuid4

import redis

from conf.config import HASH_MAX_LENGTH
from conf.config import REDIS_HOST
from conf.config import REDIS_PORT
from conf.config import REDIS_DB

redis_conn = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB
)


def generate_random_hash(max_length):
    return str(uuid4()).replace('-', '')[:max_length]


def get_hash(url):
    _hash = generate_random_hash(HASH_MAX_LENGTH)
    while redis_conn.get(_hash) is not None:
        _hash = generate_random_hash(HASH_MAX_LENGTH)

    redis_conn.set(_hash, url)
    return _hash


def get_url(_hash):
    return redis_conn.get(_hash)