from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
   Accounts = (By.XPATH, "//button[@aria-label='Account']")
   Login = (By.XPATH, "//button[@aria-label='Log in']")
   google_iframe = (By.XPATH, "//iframe[contains(@src,'accounts.google.com/gsi/button')]")
   google_email = (By.ID, "identifierId")
   # email = (By.ID, "Email")
   # password = (By.ID, "Password")
   google_email_next = (By.ID, "identifierNext")
   continuee = (By.XPATH, "//span[.='Continue']")
   google_password = (By.NAME, "Passwd")
   google_password_next = (By.ID, "passwordNext")

   def __init__(self,driver):
       super().__init__(driver)

   def click_account(self):
       self.click(self.Accounts)

   def click_login(self):
       self.click(self.Login)

   def click_google_iframe(self):
       self.click(self.google_iframe)

   def switch_to_google_window(self):
       self.main_window = self.driver.current_window_handle

       WebDriverWait(self.driver, 10).until(
           EC.number_of_windows_to_be(2)
       )

       for window in self.driver.window_handles:
           if window != self.main_window:
               self.driver.switch_to.window(window)
               break

   def enter_google_email(self,email):
       self.enter_text(self.google_email,email)

   def click_email_next(self):
       self.click(self.google_email_next)

   def enter_google_password(self, password):
       self.enter_text(self.google_password, password)

   def click_password_next(self):
       self.click(self.google_password_next)





