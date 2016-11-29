#!/usr/bin/env python
#_*_ coding=utf-8 _*_
#2016-11-13 PASS，但是没有添加附件
_author_ = 'wenzhe'
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from find_new_report import reportFile

def sendMail():
    smtpserver = 'smtp.163.com'            #发送邮件服务器
    user_account = 'chenwenzhecd@163.com'          #发送邮件邮箱，密码
    user_passsword = r"225410weyd"
    recevil_eamil = '1079610451@qq.com'         #接收邮箱
    tolist = [ '1079610451@qq.com']  #群发
    send_email = 'chenwenzhecd@163.com'        #发送邮箱
    #邮件发送主题
    subject = '好云淘活动页面!'
    #获取文件，并读取
    new_report= reportFile()            #仅是找到文件
    #print 'new_report:',new_report
    f = open(new_report,'rb')           #读取文件,用file出错
    mail_body = f.read()
    f.close()
    # 编写HTML类型的邮件正文
    msg= MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = send_email
    msg['To'] = recevil_eamil
    #连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user_account,user_passsword)
    smtp.sendmail(send_email,tolist,msg.as_string())
    smtp.quit()
    return 'mail send success!'

if __name__ == '__main__':
    sendMail()
