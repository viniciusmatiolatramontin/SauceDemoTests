import os

from selenium import webdriver
from Pages.LoginPage import LoginPage

os.environ['PATH'] += r"C:/Users/vinic/Downloads/geckodriver-v0.33.0-win64"
driver = webdriver.Firefox()

login_page = LoginPage(driver)
login_page.open_page('https://www.saucedemo.com/v1/')
login_page.enter_username('standard_user')
login_page.enter_password('secret_suus')
login_page.click_login()

assert login_page.get_error_text() == 'Epic sadface: Username and password do not match any user in this service'
