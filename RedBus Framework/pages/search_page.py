from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    from_input_click = (By.XPATH,"//div[@class='inputAndSwapWrapper___6760f0']")
    from_input = (By.XPATH,"//input[@id='srcinput']")
    From_city = (By.XPATH,"//div[contains(text(),'Jaipur (Rajasthan)')]")
    To_city = (By.XPATH,"//div[contains(text(),'Udaipur')]")
    tomorrow = (By.XPATH,"//button[@aria-label='Search for Tomorrow']")

    def __init__(self, driver):
        super().__init__(driver)

    def hover_from_input(self):
        self.hover(self.from_input_click)

    def click_from_input(self):
        self.click(self.from_input_click)

    def enter_from_city(self,city):
        self.enter_text(self.from_input,city)
        self.click(self.From_city)

    def select_to_city(self):
        self.click(self.To_city)

    def select_date_of_journey(self):
        self.click(self.tomorrow)




