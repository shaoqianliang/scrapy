import memcache

# 连接
# mc = memcache.Client(['192.168.x.x:12000'], debug=True)
# mc.set("k", "value")
# ret = mc.get('k')
# print(ret)

# 天生支持集群
mc = memcache.Client([('192.168.11.81:12000',1),], debug=True)
# ['192.168.x.1:12000','192.168.x.2:12000','192.168.x.2:12000','192.168.x.2:12000']
# # 服务器个数：2
# # 设置：key   ->  5646  -> 5646%/2
# # 获取：key   ->  5646  -> 5646%/2
# mc.set("k", "value",10)
# ret = mc.get('k')
# print(ret)
mc.set("ct", 1000)
v = mc.get('ct')
print(v,type(v))



