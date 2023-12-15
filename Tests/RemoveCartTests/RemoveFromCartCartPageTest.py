import os

from selenium import webdriver

os.environ['PATH'] += r"C:/Users/vinic/Downloads/geckodriver-v0.33.0-win64"
driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/v1/')

username = driver.find_element('id', 'user-name')
password = driver.find_element('id', 'password')
login = driver.find_element('id', 'login-button')

username.send_keys('standard_user')
password.send_keys('secret_sauce')
login.click()

for i in range(1, 7):
    add = driver.find_element('css selector', ".inventory_list > div:nth-child(" + str(i) +
                              ") > .pricebar > button")
    add.click()

cartLink = driver.find_element("css selector", ".shopping_cart_link > svg > path")
cartLink.click()

for i in range(3, 9):
    remove = driver.find_element('css selector', ".cart_list > div:nth-child(" + str(i) +
                                 ") > .cart_item_label > .item_pricebar > button")
    remove.click()


removed_cart_items = driver.find_elements("class name", "removed_cart_item")

assert len(removed_cart_items) == 6
