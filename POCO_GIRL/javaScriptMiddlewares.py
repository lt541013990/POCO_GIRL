from selenium import webdriver
from scrapy.http import HtmlResponse
import time

global  driver
driver = webdriver.PhantomJS()


class jsMiddleware(object):

    def process_request(self, request, spider):
        global driver
        driver.get(request.url)
        time.sleep(1)
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至最底端。
        time.sleep(3)
        body = driver.page_source
        print('123')
        return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)