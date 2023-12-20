from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.logout = 'logout_sidebar_link'
        self.cart = ".shopping_cart_link > svg > path"

    def get_logout_buttons(self):
        return self.driver.find_elements(By.ID, self.logout)

    def add_items(self):
        expCart = []

        for i in range(1, 7):
            add = self.driver.find_element(By.CSS_SELECTOR, ".inventory_list > div:nth-child(" + str(i) +
                                           ") > .pricebar > button")
            item = self.driver.find_element(By.CSS_SELECTOR, ".inventory_list > div:nth-child(" + str(i) +
                                            ") > .inventory_item_label > a > div")
            itemTitle = item.text
            expCart.append(itemTitle)

            add.click()

        return expCart

    def enter_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link > svg > path").click()

    def remove_items(self):
        for i in range(1, 7):
            remove = self.driver.find_element(By.CSS_SELECTOR, ".inventory_list > div:nth-child(" + str(i) +
                                         ") > .pricebar > button")

            remove.click()

