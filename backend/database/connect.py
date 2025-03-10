import os
import sys
import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config.main import config

RedisPool = redis.ConnectionPool.from_url(config.REDIS_URL)

def get_redis():
    with redis.Redis(connection_pool=RedisPool) as redis_conn:
        yield redis_conn

def get_db_engine(version='0'):
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except Exception:
        pass
    return create_engine(f'sqlite:///{os.path.join("./", "dataFiles", f"dcalc_{version}.db")}')

def get_db():
    with Session(get_db_engine()) as session:
        yield session
