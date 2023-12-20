import os

from selenium import webdriver

from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage

os.environ['PATH'] += r"C:/Users/vinic/Downloads/geckodriver-v0.33.0-win64"
driver = webdriver.Firefox()

login_page = LoginPage(driver)
login_page.open_page('https://www.saucedemo.com/v1/')
login_page.enter_username('standard_user')
login_page.enter_password('secret_sauce')
login_page.click_login()

mainPage = MainPage(driver)

mainPage.click_sort_button()
mainPage.order_by_name_az()

expTitles = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
             'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
realTitles = mainPage.iterate_titles()

assert realTitles == expTitles
