#!/usr/bin/python
# -*- ccoding:utf-8 -*-
__author__ = 'wenzhe'
# 2016-11-21 status:PASS

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
#引入ActionChains鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains

# driver= webdriver.Chrome()
# driver.set_page_load_timeout(30)
# driver.get('http://192.168.0.104:8083/wxpay104/10000/groupPurchase/mainPage')

def scroll(driver):
    '''从页面顶部滚到页面底部'''
    #scrollTop:设置或获取位于对象最顶端和窗口中可见内容的最顶端之间的距离--滚动条
    #当用户滚动指定的元素时，会发生 scroll 事件。
    #scroll 事件适用于所有可滚动的元素和 window 对象（浏览器窗口）。
    #scroolheight 是一个容器内的滚动内容（不是可视内容）的高度；就是整个内容页面的高度
    driver.execute_script("""
        (function () {
            var y = document.body.scrollTop;
            var step = 100;
            window.scroll(0, y);


            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 50);
                }
                else {
                    window.scroll(0, y);
                    document.title += "scroll-done";
                }
            }


            setTimeout(f, 1000);
        })();
        """)

