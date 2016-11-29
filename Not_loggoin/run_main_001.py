#!/usr/bin/env python
#_*_ coding=utf-8 _*_
# 2016-11-13 PASS
_author_ = 'wenzhe'

import unittest,time,sys
reload(sys)
sys.setdefaultencoding('utf-8')    #解决编码问题
from HTMLTestRunner import HTMLTestRunner
from Hyt.Not_loggoin.server.sendmail import sendMail

#指定测试目录
test_dir = './test_case'
report = './report'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m_%d %H-%M-%S")            #指定时间格式
    filename = report + '/' + now + 'result.html'       #指定报告存放位置，及命名规则
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='未登录链接测试',
                            description=u'未登录链接测试')
    runner.run(discover)
    time.sleep(2)
    fp.close()
    #sendMail()   #频繁发送会被当作垃圾处理


