# -*- coding:utf-8 -*-
import requests
from time import sleep
from threading import Thread

UPDATE_INTERVAL = 0.01

class URLThread(Thread):
    def __init__(self, url, timeout=10, allow_redirects=True):
        super(URLThread, self).__init__()
        self.url = url
        self.timeout = timeout
        self.allow_redirects = allow_redirects
        self.response = None

    def run(self):
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
            self.response = self.session.get(self.url)(self.url, timeout = self.timeout, allow_redirects = self.allow_redirects)
        except Exception , e:
            print e
            pass

def multi_get(uris, timeout=10, allow_redirects=True):
    '''
uris uri列表
timeout 访问url超时时间
allow_redirects 是否url自动跳转
'''
    def alive_count(lst):
        alive = map(lambda x : 1 if x.isAlive() else 0, lst)
        return reduce(lambda a,b : a + b, alive)
    threads = [URLThread(uri, timeout, allow_redirects) for uri in uris]
    for thread in threads:
        thread.start()
    while alive_count(threads) > 0:
        sleep(UPDATE_INTERVAL)
    return [(x.url, x.response) for x in threads]


if __name__ == '__main__':
    r = multi_get(['http://qq.com'], 1, False)
    for url, data in r:
        if data: print "received this data %s from this url %s" % (data.headers, url)