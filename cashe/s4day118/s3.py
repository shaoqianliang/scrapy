import memcache
mc = memcache.Client([('192.168.11.81:12000',1),], debug=True,cache_cas=True)
ret = mc.gets('ct')
print(ret)
v = input('>>>>')
mc.cas('ct',999)