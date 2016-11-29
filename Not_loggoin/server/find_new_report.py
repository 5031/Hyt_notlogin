#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
import os
#定义报告相对位置
def reportFile():
    report_file = 'D:\\Job\\python\\code\\Hyt\\Not_loggoin\\report'
    lists = os.listdir(report_file)     #listdir返回包含目录中条目的名称的列表
    #重新按时间对目录下的文件进行排序
    lists.sort(key=lambda fn:os.path.getmtime(report_file+ '\\' + fn))      #getmtime返回文件最后更改时间
    #print '最新文件为：' + lists[-1]
    file =os.path.join(report_file,lists[-1])                               #加入两个或多个路径名称组件，插入“\”作为所需。
    return file