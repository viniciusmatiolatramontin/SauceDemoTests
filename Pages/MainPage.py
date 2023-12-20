from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.logout = 'logout_sidebar_link'
        self.cart = ".shopping_cart_link > svg > path"
        self.sortButton = 'product_sort_container'
        self.az = "option[value='az']"
        self.za = "option[value='za']"
        self.hilo = "option[value='hilo']"
        self.lohi = "option[value='lohi']"

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

    def click_sort_button(self):
        select = self.driver.find_element(By.CLASS_NAME, self.sortButton)
        select.click()

    def order_by_name_az(self):
        option = self.driver.find_element(By.CSS_SELECTOR, self.az)
        option.click()

    def order_by_name_za(self):
        option = self.driver.find_element(By.CSS_SELECTOR, self.za)
        option.click()

    def order_by_name_hilo(self):
        option = self.driver.find_element(By.CSS_SELECTOR, self.hilo)
        option.click()

    def order_by_name_lohi(self):
        option = self.driver.find_element(By.CSS_SELECTOR, self.lohi)
        option.click()

    def iterate_titles(self):
        realTitles = []

        for i in range(1, 7):
            item = self.driver.find_element(By.CSS_SELECTOR, ".inventory_list > div:nth-child(" + str(i) +
                                            ") > .inventory_item_label > a > div")
            realTitle = item.text
            realTitles.append(realTitle)

        return realTitles

    def iterate_prices(self):
        realPrices = []

        for i in range(1, 7):
            item = self.driver.find_element('css selector', ".inventory_list > div:nth-child(" + str(i) +
                                            ") > .pricebar > div")
            realPrice = item.text
            realPrices.append(realPrice)

        return realPrices
