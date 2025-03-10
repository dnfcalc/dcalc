import json
from api.core.Gzip import gzip_zip, gzip_unzip

def get_redis_info(redis, key, fun,without_gzip=False):
    info = None
    if redis:
        try:
            if without_gzip:
                info = json.loads(redis.get(key))
            else:
                info = json.loads(gzip_unzip(redis.get(key)))
        except Exception as ex:
            print(ex)
            info = None
    if info is None:
        info = fun()
        if redis and info is not None:
            if without_gzip:
                redis.set(key, json.dumps(info))
            else:
                redis.set(key, gzip_zip(json.dumps(info)))
    return info
