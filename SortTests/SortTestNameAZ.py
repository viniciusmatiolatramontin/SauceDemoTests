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

select = driver.find_element('class name', 'product_sort_container')
select.click()
option = driver.find_element('css selector', "option[value='az']")
option.click()

expTitles = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
             'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
realTitles = []

for i in range(1, 7):
    item = driver.find_element('css selector', ".inventory_list > div:nth-child(" + str(i) +
                               ") > .inventory_item_label > a > div")
    realTitle = item.text
    realTitles.append(realTitle)

assert realTitles == expTitles
