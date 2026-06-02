from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self,locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def enter_text(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def switch_to_iframe(self,locator):
        iframe = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.switch_to.frame(iframe)

    def hover(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        # self.driver.execute_script(
        #     "arguments[0].scrollIntoView({block:'center'});",
        #     element
        # )

        actions = ActionChains(self.driver)

        actions.move_to_element(element).perform()


