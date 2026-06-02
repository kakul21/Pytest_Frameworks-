from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class SearchPage(BasePage):

    search = (By.ID,"hsw_search_button")
    hotels = (By.XPATH,"//li[@class='menu_Hotels']")
    input_click = (By.ID,"city")
    input_text = (By.XPATH,"//input[@placeholder='Where do you want to stay?']")
    select_city = (By.XPATH,"//div[@class='clickable']")
    check_in = (By.XPATH,"//div[@aria-label='Sat May 23 2026']")
    check_out = (By.XPATH,"//div[@aria-label='Sat May 30 2026']")
    apply = (By.XPATH,"//button[.='APPLY']")

    def __init__(self, driver):
        super().__init__(driver)

    def close_popup(self):
        try:
            from selenium.webdriver.common.action_chains import ActionChains
            ActionChains(self.driver).move_by_offset(0, 0).click().perform()
        except:
            pass

    def click_hotels(self):
        self.click(self.hotels)

    def click_city(self):
        self.click(self.input_click)

    def enter_city(self,input_text):
        self.enter_text(self.input_text,input_text)
        self.click(self.select_city)

    def check_in_and_out_date(self):
        self.click(self.check_in)
        self.click(self.check_out)

    def click_apply(self):
        self.click(self.apply)

    def click_search(self):
        self.click(self.search)



