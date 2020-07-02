from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

driver.get("https://www.instagram.com/leo_narita")

refreshrate = int(10)

while True:
    time.sleep(refreshrate)
    driver.refresh()
