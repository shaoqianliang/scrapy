import redis
# pool = redis.ConnectionPool(host='192.168.11.81', port=6379,)
# conn = redis.Redis(connection_pool=pool)
# conn.publish('fm104.5','sb')

redis.StrictRedis()