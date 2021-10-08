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


#bp9cbjyn j83agx80 btwxx1t3 buofh1pr i1fnvgqd hpfvmrgz
#bp9cbjyn j83agx80 btwxx1t3 buofh1pr i1fnvgqd hpfvmrgz
#bp9cbjyn j83agx80 btwxx1t3 buofh1pr i1fnvgqd hpfvmrgz
