import redis

pool = redis.ConnectionPool(host='192.168.11.81', port=6379)

conn = redis.Redis(connection_pool=pool)
# r.set('foo', '友情并阿斯顿发生地方')
# print(r.get('foo'))
# v = r.getrange('foo',0,3)
# print(v)
# v = r.strlen('foo')
# print(v)
#
# r.lpush('names','alex')
# r.lpush('names','eric')
# r.lpush('names','egon')

# v = r.lindex('names',1)
# print(v)
# aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga 0
# 
conn.zadd('zz', '友情并', -1, '阮国栋', -2,'成汤',-3)

# v = conn.zrange('zz',0,0)
# print(v[0].decode('utf-8'))
# print(v[0])
v = conn.zrank('zz',"成汤")
print(v)



