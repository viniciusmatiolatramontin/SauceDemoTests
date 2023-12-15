from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.logout = 'logout_sidebar_link'

    def get_logout_buttons(self):
        return self.driver.find_elements(By.ID, self.logout)
