#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

def nginx_502(driver):
    while 1:
        if driver.title == "502 Bad Gateway":
            driver.refresh()
        else:
            break