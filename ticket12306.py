from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(r'F:\Tools\Selenium3\chromedriver.exe')
driver.get('https://kyfw.12306.cn/otn/index/init')
driver.maximize_window()
driver.implicitly_wait(50)
driver.find_element_by_id('dc').click()
driver.find_element_by_id('fromStationText').click()
driver.find_element_by_id('fromStationText').send_keys('杭州\n')
driver.find_element_by_id('toStationText').click()
driver.find_element_by_id('toStationText').send_keys('南京\n')
# driver.find_element_by_id('train_date')
driver.find_element_by_id('a_search_ticket').click()
driver.implicitly_wait(20)
driver.find_element_by_css_selector('#date_range>ul>li:nth-child(3)').click()
driver.implicitly_wait(30)
sel = driver.find_element_by_id('cc_start_time')
tmp = Select(sel)
tmp.select_by_value('06001200')
while(True):
    driver.find_element_by_id('query_ticket')
    isticket = driver.find_element_by_id('ZE_56000G944600').text
    driver.implicitly_wait(20)
    if (isticket == '无'):
        continue
    elif (isticket == '有'):
        print('有票了!')
        break
driver.quit()
from email.mime.text import MIMEText
from email.header import Header
import smtplib

message ='''
有票了!
'''
msg = MIMEText(message,'plain','utf-8')
msg['Subject'] = Header("来自Python的邮件",'utf-8')
# msg['From'] = Header('XXXX@sina.com')
# msg['To'] = Header('receiver','utf-8')

from_addr = '1435549249@qq.com' #发件邮箱
password = 'odxnoxnjlipciffa' #邮箱密码
to_addr = '1549591113@qq.com' #收件邮箱
smtp_server = 'smtp.qq.com' #SMTP服务器，以新浪为例
try:
    server = smtplib.SMTP(smtp_server,25) #第二个参数为默认端口为25，有些邮件有特殊端口
    print('开始登录')
    server.login(from_addr,password) #登录邮箱
    print('登录成功')
    print("邮件开始发送")
    server.sendmail(from_addr,to_addr,msg.as_string())  #将msg转化成string发出
    server.quit()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("邮件发送失败",e)
