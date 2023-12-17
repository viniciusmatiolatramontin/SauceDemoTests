import os

from selenium import webdriver

from Pages.CartPage import CartPage
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
mainPage.add_items()
mainPage.enter_cart()

cartPage = CartPage(driver)
cartPage.remove_items_from_cart()

removed_cart_items = cartPage.find_removed_cart_items()

assert len(removed_cart_items) == 6
