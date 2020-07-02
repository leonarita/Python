from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

driver = 0
username = 'eunao_seimeu'
password = 'Corey5677'


class Login:

    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def sigin(self):
        print('Opening...')
        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')


        # uid = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
        #    '#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input')))

        time.sleep(3)
        uid = self.driver.find_element_by_css_selector(
            '#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input')
        uid.click()
        uid.send_keys(self.username)

        pswd = self.driver.find_element_by_css_selector(
            '#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input')
        pswd.click()
        pswd.send_keys(self.password)

        btn = self.driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4)')
        btn.click()
        time.sleep(5)


class Pageint:

    def __init__(self, driver):
        self.driver = driver


class GetPage:

    def __init__(self, driver):
        self.driver = driver

    def get_followers(self):
        flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#react-root > section > main > div > ul > li:nth-child(2) > a > span')))
        flw_btn.click()

        popup = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[4]/div/div/div[2]')))
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)


def main():
    global driver
    print('Running script...')
    driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver.exe')

    l = Login(driver, username, password)
    l.sigin()

    driver.get('https://www.instagram.com/leo_narita')
    gp = GetPage(driver)
    gp.get_followers()
    time.sleep(60)


if __name__ == '__main__':
    main()



