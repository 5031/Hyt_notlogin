#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

import unittest
from time import sleep,ctime
from selenium import webdriver
from nginx_502 import nginx_502
from second_packagin import Packagin_element
from scroll import scroll
from po import Home_Page

class TestClass(unittest.TestCase):
    # local_url = 'http://www.hyuntao.com/wxpay104/hyt/mainPage'
    # error_pic_file = "D:\\Job\\python\\code\\Hyt\\Not_loggoin\\pic\\"

    def setUp(self,local_url = 'http://www.hyuntao.com/wxpay104/hyt/mainPage',error_pic_file = "D:\\Job\\python\\code\\Hyt\\Not_loggoin\\pic\\"):
        self.driver = webdriver.Chrome()
        self.base_url = local_url
        self.driver.implicitly_wait(30)
        self.driver.get(self.base_url)
        self.error_pic_path = error_pic_file
        self.assetError = []
        nginx_502(self.driver)
        self.po =Home_Page  #仅引入了po，还需要在po中定义访问对象
        print 'test starting......'

    def tearDown(self):
        # while 1:
        #     if self.driver.title != u'好云淘':
        #         self.driver.back()
        #     else:
        #         break
        #每个测试步骤都会执行setup,所以这里的判断可以不用加
        print 'test ending......'
        self.driver.quit()

    def pinggou(self,name):

        for i in range(30):
            try:
                # 检查图片链接是否存在
                result1 = self.driver.find_element_by_css_selector( 'img[src="http://hyt-file.img-cn-hangzhou.aliyuncs.com/market/201611080839535784.png@60Q"]').get_attribute('src')
                print result1
                self.assertTrue('201611080839535784' in result1)
                break
            except:
                pass
            sleep(1)
        else:
            # for循环执行完毕了，就执行这里；for循环break后，同样不执行这里
            self.driver.get_screenshot_as_file(self.error_pic_path + name)
            self.fail('time out')

    def chuancheng(self,name):
        for i in range(30):
            try:
                result1 = self.driver.find_element_by_css_selector( 'img[src = "http://hyt-test.oss-cn-hangzhou.aliyuncs.com/companywap/images/img_laozihao.jpg"]').get_attribute( 'src')
                self.assertTrue('img_laozihao' in result1)
                break
            except:
                pass
            sleep(1)
        else:
            self.driver.get_screenshot_as_file(self.error_pic_path + name)
            self.fail('验证失败')

    def youhuiquan(self,name):
        # 查找券
        for i in range(30):
            try:
                result1 = self.driver.find_element_by_xpath('html/body/div[1]/div[2]/a[1]/div/div/div[1]/div[1]/img').get_attribute('src')
                self.assertTrue('hyt_quan' in result1)
                break
            except:
                pass
            sleep(1)
        else:
            self.driver.get_screenshot_as_file(self.error_pic_path + name)
            self.fail('time out')

    def jiudian(self,name):
        for i in range(30):
            try:
                result1 = self.driver.find_element_by_xpath( 'html/body/div[1]/div[1]/div[3]/ul/div[1]/ul/li[1]/a').get_attribute('style')
                print result1
                self.assertTrue('201611171232288545' in result1)
                break
            except:
                pass
            sleep(1)
        else:
            self.driver.get_screenshot_as_file(self.error_pic_path + name)
            self.fail('time out')

    def cloudsay(self,name):

        for i in range(30):
            try:
                result1 = self.driver.find_element_by_css_selector( 'img[src="http://hyt-file.img-cn-hangzhou.aliyuncs.com/market/201611171339011839.png"]').get_attribute('src')
                print result1
                self.assertTrue('201611171339011839' in result1)
                break
            except:
                pass
            sleep(1)
        else:
            self.driver.get_screenshot_as_file(self.error_pic_path + name)
            self.fail('time out')

    def login(self,name):
        for i in range(30):
            try:
                result1 = self.driver.find_element_by_css_selector('div[class="ol_methd"]>a span').text
                print result1
                self.assertTrue(u'微信登录' in result1)
                break
            except:
                pass
            sleep(1)
        else:
            # for循环执行完毕了，就执行这里；for循环break后，同样不执行这里
            self.driver.get_screenshot_as_file(self.error_pic_path + name)
            self.fail('time out')

    def veri_ele(self,name):

        for i in range(30):
            try:
                # css中可以写：标签.类名
                #封装方法不能调用???
                result1 = self.driver.find_element_by_css_selector('div.jh_title.hot_top').text
                print result1
                self.assertTrue(u'热门搜索' in result1)
                break
            except:
                pass
            sleep(1)
        else:
            # for循环执行完毕了，就执行这里；for循环break后，同样不执行这里
            self.driver.get_screenshot_as_file(self.error_pic_path + name)
            self.fail('time out')

    def search_name(self,serch_name,pic_name):
        for i in range(30):
            try:
                # css中可以写：标签.类名
                result1 = self.driver.find_element_by_link_text(serch_name).text
                print result1
                self.assertTrue(serch_name in result1)
                break
            except:
                pass
            sleep(1)
        else:
            # for循环执行完毕了，就执行这里；for循环break后，同样不执行这里
            self.driver.get_screenshot_as_file(self.error_pic_path + pic_name)
            self.fail('time out')

