#需要现在settings中注册
# DUPEFILTER_CLASS = 'sql.repeat_url' #默认自带的去重规则，可以自定义，参照（from scrapy.dupefilter import RFPDupeFilter）
# DUPEFILTER_DEBUG = False
# JOBDIR = "保存范文记录的日志路径，如：/root/"  # 最终路径为 /root/requests.seen

class RepeatUrl:
    def __init__(self):
        self.visited_url = set() #当前内存中的集合，可以去重，也可以解释文件或者其他服务器内存redis等

    @classmethod
    def from_settings(cls,settings): #可以从settings文件对象中获取参数
        debug = settings.getbool('DUPEFILTER_DEBUG')#可以多种方法（get，getint等）
        host = settings.getint()
        return cls()

    def request_seen(self, request):
        if request.url in self.visited_url:
            return True
        else:
            self.visited_url.add(request.url)

    def open(self):
        """
        开始爬去请求时，调用
        :return:
        """
        pass

    def close(self, reason):
        """
        结束爬虫爬取时，调用
        :param reason:
        :return:
        """
        pass

    def log(self, request, spider):
        """
        记录日志
        :param request:
        :param spider:
        :return:
        """
        pass