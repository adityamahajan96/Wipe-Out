#!/usr/bin/env python

#from __future__ import print_function
from selenium import webdriver
from bs4 import BeautifulSoup
#from argparse import ArgumentParser
from time import sleep
import getpass
import sys

driver = webdriver.Firefox()
# driver.get('https://www.facebook.com/login/')
# email_element = driver.find_element_by_id('email')
# email_element.send_keys("fakeerfaltu@gmail.com")
# password_element = driver.find_element_by_id('pass')
# password_element.send_keys("Welcome@123")
# password_element.submit()
#soup = BeautifulSoup(driver.page_source)

profile_name = "100073511051181"
user = "fakeerfaltu@gmail.com"
pswd = "Welcome@123"

if not profile_name:
    print("ERROR !!")
    sys.exit(-2)

login_page = "https://www.facebook.com/login/"
driver.get(login_page)
sleep(5)

email_ele = driver.find_element_by_name('email')
email_ele.send_keys(user)
pswd_ele = driver.find_element_by_name('pass')
pswd_ele.send_keys(pswd)
pswd_ele.submit()
sleep(2)
print("Login Done")

act_log = 'https://www.facebook.com/' + profile_name + '/allactivity?privacy_source=activity_log&log_filter=cluster_11'
driver.get(act_log)
sleep(2)

# delete = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/span")
# delete.click()
#soup = BeautifulSoup(driver.page_source)
#action = soup.find('div', {'aria-label': 'Action options'})
for i in range(2):
	driver.find_element_by_xpath("//div[@aria-label='Action options']").click()
	sleep(1)
	driver.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 btwxx1t3 buofh1pr i1fnvgqd hpfvmrgz']").click()
	sleep(1)
	driver.find_element_by_xpath("//div[@aria-label='Delete']").click()
	sleep(1)
#delete = soup.find('div', {'class': 'bp9cbjyn j83agx80 btwxx1t3 buofh1pr i1fnvgqd hpfvmrgz'})


#print("Action option: ", action)

# print(action.get('id'))
# menu_element = driver.find_element_by_id(action.get('id'))
# menu_element.click()

#sleep(5)



#action option common div:
#bp9cbjyn j83agx80 btwxx1t3 buofh1pr i1fnvgqd hpfvmrgz

#delete span:
#d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v ekzkrbhg oo9gr5id hzawbc8m

#unlike span:
#d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v ekzkrbhg oo9gr5id hzawbc8m

#recycle_bin div:
#oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 opuu4ng7 oygrvhab kj2yoqh6 cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr i1ao9s8h esuyzwwr f1sip0of lzcic4wl n00je7tq arfg74bv qs9ysxi8 k77z8yql l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn dwo3fsh8 btwxx1t3 pfnyh3mw du4w35lb