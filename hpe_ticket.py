#! /usr/bin/python3

# INSTRUCTIONS
# 1. Install Python3 for Windows 
#    https://www.python.org/downloads/release/python-380/
# 2. Download webdriver for you Chrome version Help > About Chrome
#    https://sites.google.com/a/chromium.org/chromedriver/downloads
# 3. Unzip and place the chromedriver in the same folder as the script
# 4. Install Selenium "pip install selenium"
# 5. Update input.txt with you HPE credentials

import time  
from selenium import webdriver      
from selenium.webdriver.common.keys import Keys         # Module to send keystrokes
from selenium.webdriver.support.select import Select    # Module to select drop down

# Read input_data.txt to get HPE credentials 
f = open("input.txt", "r")
user = f.readline().strip()
password = f.readline().strip()
said = f.readline().strip()
f.close()
 
# Creating an instance webdriver 
driver = webdriver.Chrome()  
# Maximizing window
driver.maximize_window()
driver.get('https://support.hpe.com/portal/site/hpsc/scm/home') 
# Wait for page to load
time.sleep(2)

# Login
#===================================
driver.find_element_by_id('username').send_keys(user)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('signIn').click()
time.sleep(10)

# Find all ids on page
#ids = driver.find_elements_by_xpath('//*[@id]')
#for i in ids:
#    # print i.tag_name
#    print(i.get_attribute('id'))

# Find the dynamic generated iframe id
iframeid = driver.find_element_by_tag_name('iframe')
# Need to switch to active iframe to find elements
driver.switch_to.frame(iframeid.get_attribute('id'))
# Provide SAID
driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_txtSubmitCase').send_keys(said)
driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_btnSubmitCase').click()  
time.sleep(15)

# Fill in default case details entries
#=====================================
# Find the dynamic generated iframe id
iframeid = driver.find_element_by_tag_name('iframe')
# Need to switch to active iframe to find elements
driver.switch_to.frame(iframeid.get_attribute('id'))
# Populate default entries in case details
driver.find_element_by_id('environmentsList').send_keys("Red Hat Enterprise Linux")
driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_txtContactHoursORTimezone').send_keys('8am-5pm CT')





