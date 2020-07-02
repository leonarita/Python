from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)
driver.get('https://www.facebook.com/')

username = "your_username"
password = "your_password"

UN = driver.find_element_by_id('email')

UN.send_keys(username)

PS = driver.find_element_by_id('pass')

PS.send_keys(password)

LI = driver.find_element_by_id('loginbutton')

LI.click()