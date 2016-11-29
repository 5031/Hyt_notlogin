# _*_ coding=utf-8 _*_
from selenium import webdriver
import unittest, time
from time import sleep
from pytesseract import pytesseract

class WebTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.hyuntao.com/wxpay104/hyt/mainPage")
        print 'Test Start....'

    def tearDown(self):
        self.driver.quit()
        print 'Test End@@@@@@'

    def test_1(self):
        '''搜索测试：检查搜索页面的"热门搜索"字段是否存在'''
        self.driver.find_element_by_css_selector('a.in_search_tap').click()
        for i in range(60):
            try:
                #css中可以写：标签.类名
                result1 = self.driver.find_element_by_link_text('护肤').text
                print result1
                self.assertTrue(u'护肤' in result1)
                break
            except:
                pass
            sleep(1)
        else:
            # for循环执行完毕了，就执行这里；for循环break后，同样不执行这里
            self.driver.get_screenshot_as_file("D:\\Job\\python\\code\\Hyt\\Not_loggoin\\pic\\test.png")
            self.fail('time out')


if __name__ == '__main__':
    unittest.main()