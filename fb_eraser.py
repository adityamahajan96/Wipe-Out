#!C:/Python310/python.exe 
#print("Content-Type: text/html\n") 
#print('Hello') 
import cgi
from selenium import webdriver
#print('Hello2') 
#from bs4 import BeautifulSoup
#from argparse import ArgumentParser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#print('Hello3')
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#print('Hello4')
import time
from time import sleep
import getpass
import sys
sys.stdout.write('Content-Type: text/html;charset=utf-8\r\n\r\n')
#print('Hello5')

form = cgi.FieldStorage()
profile_name = form.getvalue('username')
pswd = form.getvalue('password')

cnt1 = form.getvalue('del_count')
cnt2 = form.getvalue('cnt')
#print(type(cnt1), cnt2)

n = 1
if int(cnt1) > 0:
    n = int(cnt1)
else:
    n = int(cnt2)
#print(n)

#print(pswd)

driver = webdriver.Firefox(executable_path = 'C:/Users/Suman Mitra/Desktop/OP Project/geckodriver-v0.30.0-win64/geckodriver.exe')

# profile_name = input("Please enter your FB username (not Email): ")
# pswd = getpass.getpass(prompt = "Password: ")
# if not profile_name:
    # print("ERROR !!")
    # sys.exit(-2)

login_page = "https://www.facebook.com/login/"
driver.set_window_size(680, 920)
#driver.manage().window().setPosition(new Point(680, 0))
driver.get(login_page)
sleep(5)
#print('Before Try')
try:
    #print('Try 1')
    email_ele = driver.find_element_by_name('email')
    email_ele.send_keys(profile_name)
    pswd_ele = driver.find_element_by_name('pass')
    pswd_ele.send_keys(pswd)
    pswd_ele.submit()
    sleep(3)
    print('<html>')
    print('<head><meta name="viewport" content="width=device-width, initial-scale=1">')
    print('<link rel="stylesheet" href="css/style.css"></head>')
    print('<body>')
    print('<div class="log">')
    print('<div class="imgcontainer" id="img_con"><img src="images/wipeout_logo.jpeg" alt="WipeOut" class="avatar" loading="lazy"></div>')
    print('<div class="demo_login"><div class="print">LOGIN Successful...</div></div>')
    sys.stdout.flush()
    sleep(1)
    print('<div class="demo_welcome"><div class="print_welcome">Welcome User - <b>' + profile_name + '</b></div></div>')
    sys.stdout.flush()
except:
    print('<div class="demo_error"><div class="print">INVALID Username / Password !! Exitting...</div></div>')
    sys.stdout.flush()
    sys.exit("Exitting !!")
    driver.close()

try:
    act_log = 'https://www.facebook.com/' + profile_name + '/allactivity?privacy_source=activity_log&log_filter=cluster_11'
    driver.get(act_log)
    sleep(2)
    print('<div class="demo"><div class="print">User - <b>' + profile_name + '</b> Activity log opened..</div></div>')
    sys.stdout.flush()
except:
    print('<div class="demo_error"><div class="print">ERROR opening the Activity Log page. LOGGING OUT...</div></div>')
    driver.close()

# delete = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/span")
# delete.click()
#soup = BeautifulSoup(driver.page_source)
#action = soup.find('div', {'aria-label': 'Action options'})
for i in range(n):
    try:
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Action options']"))).click()
        #driver.find_element_by_xpath("//div[@aria-label='Action options']").click()
        sleep(4)
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='bp9cbjyn j83agx80 btwxx1t3 buofh1pr i1fnvgqd hpfvmrgz']"))).click()
        sleep(4)
        try:
            WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Delete']"))).click()
            print('<div class="demo"><div class="print">Activity-' + str(i + 1) + ' Deleted !!</div></div>')
            sys.stdout.flush()
            sleep(4)
        except:
            act_log = 'https://www.facebook.com/' + profile_name + '/allactivity?privacy_source=activity_log&log_filter=cluster_11'
            print('<div class="demo"><div class="print">Activity-' + str(i + 1) + ' Deleted !!</div></div>')
            driver.get(act_log)
            sleep(4)
            continue
    except:
        print('<div class="demo_error"><div class="print">TIMEOUT !! Please check your Internet Connection. LOGGING OUT...\n</div></div>')
        driver.close()
print('<div class="demo_welcome"><div class="print_welcome">User - <b>' + profile_name + '</b> LOGGING OUT...</div></div>')
print('<div class="redirect"><a href="#" onclick="javascript:window.history.back(-1);return false;">Go Back to Login Page</a></div>')
print('</div></body></html>')
driver.close()