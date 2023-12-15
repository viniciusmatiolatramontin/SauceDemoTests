from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = 'user-name'
        self.password = 'password'
        self.login = 'login-button'
        self.error = "h3[data-test='error']"

    def open_page(self, url):
        self.driver.get(url)

    def click_login(self):
        self.driver.find_element(By.ID, self.login).click()

    def enter_username(self, name):
        self.driver.find_element(By.ID, self.username).send_keys(name)

    def enter_password(self, pswrd):
        self.driver.find_element(By.ID, self.password).send_keys(pswrd)

    def get_error_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.error).text
