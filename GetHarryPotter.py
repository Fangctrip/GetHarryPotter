import requests
from lxml import etree
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': 'ua.random'}
link = []
def GetLink(url):  #获取每一个章节的链接
    r = requests.get(url,headers=headers).text
    s = etree.HTML(r)
    li =  s.xpath('//div[@class="m-chapter m-chapter-2"]/ul/li/div/a/@href')
    for i in li:
        link.append('http://www.en8848.com.cn' + i)
    return link

def GetContent(chapter):  #获取内容，并写入txt
    r = requests.get(chapter, headers=headers).text
    s = etree.HTML(r)
    content = s.xpath('//div[@class="m-introbox"]/p/text()')
    #print(content)
    with open('harry.txt','a+',encoding='utf-8') as f:
        for i in content:
            f.write(i)

#因为网页http://www.en8848.com.cn/fiction/Fiction/Children/637.html，上只有5个章节
for i in (
    'http://www.en8848.com.cn/fiction/Fiction/Children/637.html',
    'http://www.en8848.com.cn/fiction/Fiction/Fantasy/58488.html',
    'http://www.en8848.com.cn/fiction/Fiction/Children/636.html',
    'http://www.en8848.com.cn/fiction/Fiction/Children/635.html',
    'http://www.en8848.com.cn/fiction/Fiction/Children/634.html',):
    GetLink(i)
for i in link:
    GetContent(i)
