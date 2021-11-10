#!/usr/bin/env python

from selenium import webdriver
from bs4 import BeautifulSoup
#from argparse import ArgumentParser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
import getpass
import sys

driver = webdriver.Firefox(executable_path = 'C:/Users/Suman Mitra/Desktop/OP Project/geckodriver-v0.30.0-win64/geckodriver.exe')

# driver.get('https://www.facebook.com/login/')
# email_element = driver.find_element_by_id('email')
# email_element.send_keys("fakeerfaltu@gmail.com")
# password_element = driver.find_element_by_id('pass')
# password_element.send_keys("Welcome@123")
# password_element.submit()
#soup = BeautifulSoup(driver.page_source)

#profile_name = "samast.parivaar"
#user = "fakeerfaltu@gmail.com"
#pswd = "Welcome@1234"

profile_name = input("Please enter your FB username (not Email): ")
pswd = getpass.getpass(prompt = "Password: ")
if not profile_name:
    print("ERROR !!")
    sys.exit(-2)

login_page = "https://www.facebook.com/login/"
driver.get(login_page)
sleep(5)
try:
    email_ele = driver.find_element_by_name('email')
    email_ele.send_keys(profile_name)
    pswd_ele = driver.find_element_by_name('pass')
    pswd_ele.send_keys(pswd)
    pswd_ele.submit()
    sleep(3)
    print("Login Successful...")
except:
    print("\nINVALID Username / Password !!")
    sys.exit("Exitting !!")

try:
    act_log = 'https://www.facebook.com/' + profile_name + '/allactivity?privacy_source=activity_log&log_filter=cluster_11'
    driver.get(act_log)
    sleep(2)
    print("User: <" + profile_name + "> Activity log opened..")
except:
    print("ERROR opening the Activity Log page...")
    sys.exit("Exitting !!")

# delete = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/span")
# delete.click()
#soup = BeautifulSoup(driver.page_source)
#action = soup.find('div', {'aria-label': 'Action options'})
for i in range(1):
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Action options']"))).click()
        #driver.find_element_by_xpath("//div[@aria-label='Action options']").click()
        sleep(2)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='bp9cbjyn j83agx80 btwxx1t3 buofh1pr i1fnvgqd hpfvmrgz']"))).click()
        sleep(2)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Delete']"))).click()
        print("Activity-" + str(i + 1) + " Deleted !!")
        sleep(1)
    except:
        print("\n TIMEOUT EXCEPTION !! Please check your Internet Connection...\n")
