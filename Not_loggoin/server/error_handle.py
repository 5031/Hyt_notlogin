#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
import unittest

class Error_handle(unittest):
    def __init__(self,driver,cmparename,picname):
        self.driver = driver
        self.cmparename = cmparename
        self.picname = picname

    def error_verifaction(self):
        if self.driver.title == "502 Bad Gateway":
            self.driver.refresh()
        else:
            try:
                self.assertEqual(self.driver.title, self.cmparename)
            except AssertionError as e:
                self.driver.get_screenshot_as_file("D:\\Job\\python\\code\\Hyt\\Not_loggoin\\pic\\" + self.picname)
                self.assertEqual(self.driver.title,self.cmparename)

    def nginx_502(driver):
        while 1:
            if driver.title == "502 Bad Gateway":
                driver.refresh()
            else:
                break