#-*- coding:utf-8 -*-
import requests
import json
import urllib
import urllib2

from lxml import etree

class CustomSprider:
    def analysisHtml(self):
        self.url ="https://www.baidu.com"
        self.headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;",
                    "Accept-Encoding":"gzip",
                    "Accept-Language":"zh-CN,zh;q=0.8",
                    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
        }
        self.session = requests.Session()
        self.session.verify = False #关闭https验证
        self.session.headers = self.headers
        try:
           self.resp_json = self.session.get(self.url)
           # self.datas = json.loads(self.resp_json.text)["data"]
           # return self.datas
           return self.resp_json.text
        except Exception,e:
           print e
    def test(self,html):
        selector = etree.HTML(html)
        #提取属性
        link = selector.xpath('//a/@href')
        for each in link:
             print each
def run():
    sprider = CustomSprider()
    res = sprider.analysisHtml()
    sprider.test(res)
    # for i, info in enumerate(res):
    #     print "-------------------"
    #     print u"名称:%s" %info["name"]
    #     print "-------------------"

if __name__ == '__main__':
    run()