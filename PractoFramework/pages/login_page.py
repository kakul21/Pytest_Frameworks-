from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    login = (By.XPATH, "//a[.='Login / Signup']")
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.ID, "login")


    def __init__(self, driver):
        super().__init__(driver)

    def click_login(self):
        self.click(self.login)

    def enter_username(self,username):
        self.enter_text(self.username,username)

    def enter_password(self,password):
        self.enter_text(self.password,password)

    def click_login_button(self):
        self.click(self.login_button)