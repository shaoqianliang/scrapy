import requests,re
from bs4 import BeautifulSoup
import pymysql
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Referer':'https: // www.baidu.com / link?url = 6aILAtgKvYMWuJJ - 9e_a - dBz8OmupNSKiSmvKRQdqrQyU9UmvDUEWP5B9MyRyobf & wd = & eqid = d477b8460003e364000000065ad2fa30'}
conn = pymysql.connect(host='localhost', port=3306, user='root', password='891008', db='爬虫',charset='utf8mb4')  # 这里是utf8不是utf-8注意
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 默认是元祖，转换成字典格式
page = 1
Flag = True
while Flag:
    url = 'https://www.qiushibaike.com/8hr/page/{}/'.format(page)
    rel = requests.get(url,params = headers)
    soup = BeautifulSoup(rel.text,'html.parser')
    max_page = soup.find(name='ul',class_="pagination").find_all('span')[-2].text
    item = soup.find_all(attrs={'id':re.compile('qiushi_tag_(\d+)')})
    for rel in item:
        auth = rel.find('h2').text
        text = rel.find('div',class_='content').text
        result = re.sub('\n*|\t*', '',text) #替换
        # """try:
        #     co = re.compile(u'[\U00010000-\U0010ffff]') #过滤emoji表情（4位字节的utf8mb4,真正utf81-6个字节）
        # except re.error:
        #     co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        # result = co.sub('',result)
        # result = re.findall('\n*|\t*',text)"""
        print(auth,'\n',result)
        # text = pymysql.escape_string(text)
        cur.execute("""INSERT INTO 百度糗事 VALUES ("%s",'"%s"')""" %(auth,result))
    page += 1
    if page > int(max_page):
        Flag = False
cur.close()
conn.commit()
conn.close()