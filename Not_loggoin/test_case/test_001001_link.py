#!/usr/bin/env python
#_*_ coding=utf-8 _*_
# a标签点击问题 11-11 fail
_author_ = 'wenzhe'
import os,sys,time,unittest
from time import sleep,ctime
from Hyt.Not_loggoin.server.testcalss import TestClass
from selenium.webdriver.support.ui import WebDriverWait


class Test_all_link(TestClass):
    '''测试没有登录，各处链接跳转是否有效'''

    def test_001(self):
        '''点击首页-购物车链接,通过登录中的“微信提示”语判断'''
        self.driver.find_element_by_class_name('in_cart_icon').click()
        self.login('error_pic_001.png')

    def test_002(self):
        '''点击首页-抢购链接，验证抢购title是否正确'''
        js = "$(\"a[class = 'newpg in_pg1']\").click();"
        self.driver.execute_script(js)
        sleep(3)
        print self.driver.title
        try:
            self.assertEqual(self.driver.title, u'抢购')
        except AssertionError as e:
            self.driver.get_screenshot_as_file(self.error_pic_path+"error_pic_002.png")
            self.assertEqual(self.driver.title, u'抢购')

    def test_003(self):
        '''点击首页-拼购,验证第一个拼购“土猪测试”主图是否存在'''
        js = "$(\'a[class=\"newpg in_pg2\"]\').click()"
        self.driver.execute_script(js)
        self.pinggou("error_pic_003.png")

    def test_004(self):
        '''点击首页-传承，验证“老字号”图片是否存在'''
        js = "$(\'a[class=\"newpg in_pg3\"]\').click()"
        self.driver.execute_script(js)
        self.chuancheng('"error_pic_004.png"')

    def test_005(self):
        '''点击首页-品牌-第一个，验证“猕猴桃”介绍是否存在'''
        js = "$(\'ul[class=\"brand_ul\"]>li>a\').eq(0).click()"
        self.driver.execute_script(js)
        for i in range(60):
            try:
                result1 = self.driver.find_element_by_class_name('pinpai_jieshao').text
                self.assertTrue(u'异珍源猕猴桃介绍' in result1)
                break
            except:
                pass
            sleep(1)
        else:
            self.driver.get_screenshot_as_file(self.error_pic_path+"error_pic_005.png")
            self.fail('验证失败')

    def test_006(self):
         '''点击首页-优品,进入“潼川豆豉”优品详情，验证第一个图片中文字是否存在'''
         self.driver.find_element_by_xpath('html/body/div[3]/ul/li[2]/a/img').click()
         sleep(2)
         self.driver.find_element_by_xpath('html/body/div[2]/div[3]/ul/li[1]/div/img').click()
         for i in range(60):
             try:
                 # result1 = self.driver.find_element_by_xpath('html/body/div[2]/div[4]/ul/li[1]/div/div/div/p').text
                 result1 = self.driver.find_element_by_xpath('html/body/div[2]/div[4]/ul/li[1]/div/div/div/p').text
                 print result1
                 self.assertTrue(u'无论是作主料' in result1)
                 break
             except:
                 pass
             sleep(1)
         else:
            self.driver.get_screenshot_as_file(self.error_pic_path+"error_pic_006.png")
            self.fail('验证失败')

    def test_007(self):
        '''点击首页-发现，进入拼购，仅判断“土猪测试”拼购是否存在'''
        #点击发现
        self.driver.execute_script("$(\'div[class=\"my_foot_nav\"]>ul>li>a\').eq(2).click()")
        #点击拼购
        self.driver.execute_script("$(\'div[class=\"fx_foot_nav\"]>ul>li>a\').eq(0).click()")
        self.pinggou("error_pic_007.png")

    def test_008(self):
        '''点击首页-发现，进入传承，判断“老字号”图片是否存在'''
        self.driver.execute_script("$(\'div[class=\"my_foot_nav\"]>ul>li>a\').eq(2).click()")
        self.driver.execute_script("$(\'div[class=\"fx_foot_nav\"]>ul>li>a\').eq(1).click()")
        self.chuancheng("error_pic_008.png")

    def test_009(self):
        '''点击首页-发现，进入领券中心，通过“自动化优惠券”图标链接是否存在'''
        self.driver.execute_script("$(\'div[class=\"my_foot_nav\"]>ul>li>a\').eq(2).click()")
        self.driver.execute_script("$(\'div[class=\"fx_foot_nav\"]>ul>li>a\').eq(2).click()")
        self.youhuiquan("error_pic_009.png")

    @unittest.skip("跳过测试")
    def test_010(self):
        '''酒店易错，暂时被注释；点击首页-发现，进入酒店，判断“自动化酒店”图片是否存在'''

        # self.driver.execute_script("$(\'div[class=\"my_foot_nav\"]>ul>li>a\').eq(2).click()")
        # self.driver.execute_script("$(\'div[class=\"fx_foot_nav\"]>ul>li>a\').eq(3).click()")
        # self.jiudian("error_pic_010.png")

    def test_011(self):
        '''点击首页-云说，进入云说，判断“Auto_test_云说_别删”图片是否存在'''
        self.driver.execute_script("$(\'div[class=\"my_foot_nav\"]>ul>li>a\').eq(3).click()")
        self.cloudsay("error_pic_011.png")

    def test_012(self):
        '''点击首页-个人中心，进入登录，判断：微信提示语'''
        self.driver.execute_script("$(\'div[class=\"my_foot_nav\"]>ul>li>a\').eq(4).click()")
        self.login("error_pic_012.png")

    def test_013(self):
        ''''搜索测试：检查搜索页面的"热门搜索"字段是否存在'''
        self.driver.find_element_by_css_selector('div.focusdiv').click()
        self.veri_ele("error_pic_013.png")

    def test_014(self):
        '''点击首页--分类，判断护肤分类是否存在'''
        self.driver.find_element_by_css_selector('a.in_search_tap').click()
        self.search_name("护肤","error_pic_014.png")

    def test_015(self):
        '''检查首页顶部的下载按钮是否存在'''
        self.search_name("下载安装", "error_pic_015.png")