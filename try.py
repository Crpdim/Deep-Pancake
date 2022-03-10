from time import sleep
from tkinter import Button
import itertools as its
from selenium import webdriver
words = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

browser = webdriver.Chrome()
browser.get('http://192.168.1.1')
sleep(1)
userID = browser.find_element_by_id("username")
userPASSWORD = browser.find_element_by_xpath("//input[@type='password']")
But = browser.find_element_by_id("login-btn")
userID.send_keys("admin")
userPASSWORD.send_keys('admin')
But.click()
sleep(1)
browser.get_screenshot_as_file('screenshot/123.png')
# re = 5
# while 2>1:
#     r = its.product(words,repeat=re)
#     for i in r:
#         # print(type(i))
#         a ="".join(i)        ##通过.join将数组里面的元素转换成字符串
#         userPASSWORD.send_keys(a)
#         print("当前测试密码:",a)
#         But.click()
#         sleep(1)
#         userPASSWORD.clear()
        
#     else:
#         re+1




# print(browser.page_source)