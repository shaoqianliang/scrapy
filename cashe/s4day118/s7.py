import redis
pool = redis.ConnectionPool(host='192.168.11.81', port=6379)
conn = redis.Redis(connection_pool=pool)
pb = conn.pubsub()
pb.subscribe('fm104.5')


while True:
    msg = pb.parse_response()
    print(msg)