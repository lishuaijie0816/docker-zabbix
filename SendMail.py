# -*- coding: UTF-8 -*-
'''
发送txt文本邮件
'''
import smtplib
import sys
from email.mime.text import MIMEText
from email.header import Header

reload(sys)
sys.setdefaultencoding('utf-8')

a = str(sys.argv[1])
b = str(sys.argv[2])
c = str(sys.argv[3])
#mailto_list=[""] 
mailto_list = a.split(";")
mail_host="smtp.exmail.qq.com"  #设置服务器
mail_user="shuaijie.li@newtranx.com"    #用户名
mail_pass="LiShuaiJie0816"   #口令 
mail_postfix="newtranx.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  
    me= str("Zabbix<")+mail_user+str(">")
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    #msg['To'] = mailto_list
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  
if __name__ == '__main__':  
    if send_mail(mailto_list,str(b),str(c)):  
        print "发送成功"  
    else:  
        print "发送失败"

