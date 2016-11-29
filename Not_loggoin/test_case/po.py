#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
"""通过page object设计模式来实现
    定义页面操作基本方法"""
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

class Page(object):
    login_url = 'http://www.hyuntao.com/wxpay104/10000/hyt/mainPage'
    def __init__(self,driver,base_url=login_url):
        self.base_url = base_url
        self.driver = webdriver.Chrome()
        self.timeout = 30

    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)

    def open(self):   #调用_open打开URL网站
        self._open(self.url)

    def find_element(self,*loc):        #定位元素
        return self.driver.find_element(*loc)