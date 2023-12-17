from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def iterate_cart(self):
        realCart = []

        for i in range(3, 9):
            item = self.driver.find_element(By.CSS_SELECTOR, ".cart_list > div:nth-child(" + str(i) +
                                            ") > .cart_item_label > a > div")
            itemTitle = item.text
            realCart.append(itemTitle)

        return realCart

    def remove_items_from_cart(self):
        for i in range(3, 9):
            remove = self.driver.find_element(By.CSS_SELECTOR, ".cart_list > div:nth-child(" + str(i) +
                                              ") > .cart_item_label > .item_pricebar > button")
            remove.click()

    def find_removed_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "removed_cart_item")

    def find_cart_items(self):
        return self.driver.find_elements("class name", "cart_item")
