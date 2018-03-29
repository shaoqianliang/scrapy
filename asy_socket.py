# -*- coding: utf-8 -*-
import socket,select
class Request(object):
    def __init__(self,sock,info):
        self.sock = sock
        self.info = info
    def fileno(self):
        return self.sock.fileno()
class asyio(object):
    def __init__(self):
        self.sock_list =[]
        self.conns = []
    def add_request(self,req_url):
        """
        创建请求
        :return:
        """
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect((req_url['host'],req_url['port'])) #必须带括号host和port一个整体
        except BlockingIOError as e:
            obj = Request(sock,req_url) #获取多属性，重新封装对象socket
            self.sock_list.append(obj)
            self.conns.append(obj)
            pass
    def run(self):
        """开始检测连接"""

        while True:
            r, w, e =select.select(self.sock_list,self.conns,[],0.5) #封装任何对象，但是必须要有fileno方法
            for obj in w: #w可能是几个域名返回的对象也可能为空
                #检测访问的是哪个域名
                data = "GET %s http/1.1\r\nhost:%s\r\n" %(obj.info['path'],obj.info['host'])
                obj.sock.send(data.encode('utf-8')) #调用对象中的对象方法
                self.conns.remove(obj)#接收到数据 溢出防止二次发送
            for obj in r:
                response = obj.sock.recv(8096)
                print(obj.info['host'],response)
                self.sock_list.remove(obj)
            if not self.sock_list:
                break
url_list = [
    {'host':'www.github.com','port':80,'path':'/'},
    {'host':'www.bing.com','port':80,'path':'/'},
    {'host':'www.zhihu.com','port':80,'path':'/'}
]
obj = asyio()
for item in url_list:
    obj.add_request(item)  #开始发送请求
obj.run()
