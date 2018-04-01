from scrapy.utils import request
from scrapy.http import Request


obj1 = Request(url='http://www.baidu.com?id=1&name=3')
obj2 = Request(url='http://www.baidu.com?name=3&id=1')

v = request.request_fingerprint(obj1)
print(v)
v = request.request_fingerprint(obj2)
print(v)