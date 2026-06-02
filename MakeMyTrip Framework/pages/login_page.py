from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    login_page = (By.XPATH, "//li[@class='makeFlex hrtlCenter font12 makeRelative lhUser userLoggedOut']")
    google_iframe = (By.XPATH, "//iframe[contains(@src,'accounts.google.com/gsi/button')]")
    google_button = (By.XPATH, "//div[@class='nsm7Bb-HzV7m-LgbsSe-Bz112c']")
    google_email = (By.ID, "identifierId")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    google_email_next = (By.ID, "identifierNext")
    continuee = (By.XPATH, "//span[.='Continue']")
    google_password = (By.NAME, "Passwd")
    google_password_next = (By.ID, "passwordNext")

    def close_popup(self):
        try:
            from selenium.webdriver.common.action_chains import ActionChains
            ActionChains(self.driver).move_by_offset(0, 0).click().perform()
        except:
            pass

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_button(self):
        self.click(self.login_page)

    def click_login(self):
        self.switch_to_iframe(self.google_iframe)

    def click_google_signin(self):
        self.click(self.google_button)

    def switch_to_google_window(self):
        self.main_window = self.driver.current_window_handle

        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(2)
        )

        for window in self.driver.window_handles:
            if window != self.main_window:
                self.driver.switch_to.window(window)
                break

    def enter_google_email(self, email):
        self.enter_text(self.google_email, email)

    def click_email_next(self):
        self.click(self.google_email_next)

    def enter_google_password(self, password):
        self.enter_text(self.google_password, password)

    def click_password_next(self):
        self.click(self.google_password_next)



