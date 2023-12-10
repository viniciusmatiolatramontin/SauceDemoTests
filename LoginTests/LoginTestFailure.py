import os

from selenium import webdriver

os.environ['PATH'] += r"C:/Users/vinic/Downloads/geckodriver-v0.33.0-win64"
driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/v1/')

username = driver.find_element('id', 'user-name')
password = driver.find_element('id', 'password')
login = driver.find_element('id', 'login-button')

username.send_keys('standard_user')
password.send_keys('secret_suus')
login.click()

error = driver.find_element('css selector', "h3[data-test='error']")

assert error.text == 'Epic sadface: Username and password do not match any user in this service'
