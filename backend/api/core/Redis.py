import json
from api.core.Gzip import gzip_zip, gzip_unzip
from config.main import config

def get_redis_info(redis, key, fun,without_gzip=False):
    info = None
    if redis and not config.DEBUG_MODE:
        try:
            if without_gzip:
                info = json.loads(redis.get(key))
            else:
                info = json.loads(gzip_unzip(redis.get(key)))
        except Exception:
            info = None
    if info is None:
        info = fun()
        if redis and info is not None:
            if without_gzip:
                redis.set(key, json.dumps(info))
            else:
                redis.set(key, gzip_zip(json.dumps(info)))
    return info
