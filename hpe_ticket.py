#!/usr/bin/python3

# INSTRUCTIONS
# 1. Install Python3 for Windows 
#    https://www.python.org/downloads/release/python-380/
# 2. Download webdriver for you Chrome version Help > About Chrome
#    https://sites.google.com/a/chromium.org/chromedriver/downloads
# 3. Unzip and place the chromedriver in the same folder as the script
# 4. Install Selenium "pip install selenium"
# 5. Update input.txt with your HPE credentials

import time  
from selenium import webdriver      
from selenium.webdriver.common.keys import Keys                     # Module to send keystrokes
from selenium.webdriver.support.ui import WebDriverWait             # Module to proceed when page loaded
from selenium.webdriver.support import expected_conditions as EC    # Used by WebDriveWait module
from selenium.webdriver.common.by import By                         # Used by WebDriveWait module
#from selenium.webdriver.support.select import Select                # Module to select option drop down

# Read input_data.txt to get HPE credentials 
f = open("input.txt", "r")
user = f.readline().strip()
password = f.readline().strip()
said = f.readline().strip()
f.close()
 
# Creating a webdriver instance  
driver = webdriver.Chrome()  
# Maximize window
driver.maximize_window()
driver.get('https://support.hpe.com/portal/site/hpsc/scm/home') 
# Wait for page to load (blocking)
#time.sleep(2)

# Wait for page to load max 2s or until id "username" is located
WebDriverWait(driver,2).until(EC.presence_of_element_located((By.ID,"username")))

# Login
#===================================
driver.find_element_by_id('username').send_keys(user)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('signIn').click()
#time.sleep(10)

# Print all ids on page
#ids = driver.find_elements_by_xpath('//*[@id]')
#for i in ids:
#    # print i.tag_name
#    print(i.get_attribute('id'))

# Wait for page to load max 10s or until id "iframe" is located
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"iframe")))

# Find the dynamic generated iframe id
iframeid = driver.find_element_by_tag_name('iframe')
# Need to switch to active iframe to find expected elements
driver.switch_to.frame(iframeid.get_attribute('id'))
# Provide SAID
driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_txtSubmitCase').send_keys(said)
driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_btnSubmitCase').click()  
#time.sleep(15)

# Wait for page to load max 15s or until id "iframe" is located
WebDriverWait(driver,15).until(EC.presence_of_element_located((By.TAG_NAME,"iframe")))

# Fill in default case details entries
#=====================================
# Find the dynamic generated iframe id
iframeid = driver.find_element_by_tag_name('iframe')
# Need to switch to active iframe to find expected elements
driver.switch_to.frame(iframeid.get_attribute('id'))

# Click email radio button
driver.find_element_by_xpath('//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_preferredContactUpdPanel"]/table/tbody/tr[2]/td[1]/a').click()
# Add time delay to avoid select/input issues
time.sleep(0.5)

# Click Severity drop down
driver.find_element_by_xpath('//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_ddlSeverity_title"]/tr/td[2]/span').click()
time.sleep(0.5)

# Select 3-Normal
driver.find_element_by_xpath('//*[@id="ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_ddlSeverity_child"]/ul/li[2]/span').click()
time.sleep(0.5)

# Operating system/version
driver.find_element_by_id('environmentsList').send_keys("Red Hat Enterprise Linux")
time.sleep(0.5)

# Contact hours/time zone
driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_txtContactHoursORTimezone').send_keys('8am-5pm ET/CT')
time.sleep(0.5)

# Site access details
driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_txtGSDSiteAccess').send_keys("Contact ticket issuer for details")
time.sleep(0.5)

# Problem description template
driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_txtAreaCDProbDesc').send_keys('Description:\n\nActual Behavior:\n\nExpected Behavior:\n\nSteps to Reproduce:\n')
time.sleep(0.5)

# Troubleshooting steps taken template
driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder3Col_txtAreaCDSteps').send_keys('Troubleshooting Steps Attempted:\n\nWorkaround:\n')
