#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
#暂时没用这个
#封装查找元素组
class Packagin_element(object):
    def fid(driver,value):
        id = driver.find_element_by_id('value')
        return id

    def fname(driver,value):
        id = driver.find_element_by_name('value')
        return id

    def fclname(driver, value):
        id = driver.find_element_by_class_name('value')
        return id

    def fcss(driver, value):
        id = driver.find_element_by_css_selector('value')
        return id

    def flink(driver, value):
        id = driver.find_element_by_link_text('value')
        return id

    def fparlink(driver, value):
        id = driver.find_element_by_partial_link_text('value')
        return id

    def ftag(driver, value):
        id = driver.find_element_by_tag_name('value')
        return id

    def fxpath(driver, value):
        id = driver.find_element_by_xpath('value')
        return id

    def fsid(driver, value):
        id = driver.find_elements_by_id('value')
        return id

    def fsname(driver, value):
        id = driver.find_elements_by_name('value')
        return id

    def fsclname(driver, value):
        id = driver.find_elements_by_class_name('value')
        return id

    def fscss(driver, value):
        id = driver.find_element_by_css_selector('value')
        return id

    def fslink(driver, value):
        id = driver.find_elements_by_link_text('value')
        return id

    def fsparlink(driver, value):
        id = driver.find_elements_by_partial_link_text('value')
        return id

    def fstag(driver, value):
        id = driver.find_elements_by_tag_name('value')
        return id

    def fxpath(driver, value):
        id = driver.find_elements_by_xpath('value')
        return id