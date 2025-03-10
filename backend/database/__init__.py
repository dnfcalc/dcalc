import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)