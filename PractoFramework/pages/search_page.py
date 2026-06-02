from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    city = (By.XPATH,"(//div[@class='c-omni-searchbox_wrapper ']//input)[1]")
    select_city = (By.XPATH,"(//div[@class='c-omni-suggestion-item'])[1]")
    # cross = (By.XPATH,"//i[@class='icon-ic_cross_solid']")
    speciality = (By.XPATH,"(//div[@class='c-omni-suggestion-item'])[3]")
    gender = (By.XPATH, "(//div[@class='c-filter__box u-pos-rel c-dropdown'])[1]")
    female = (By.XPATH, "(//li[@class='c-dropdown__list__item'])[2]")
    experience = (By.XPATH, "(//div[@class='c-filter__box u-pos-rel c-dropdown'])[2]")
    years_of_experience = (By.XPATH, "(//li[@class='c-dropdown__list__item'])[5]")
    booking = (By.XPATH, "(//button[@class='u-t-capitalize u-bold u-round-corner--large c-btn--dark-medium'])[4]")
    day = (By.XPATH,"(//div[@class='pure-u-1-3 c-day-label '])[1]")
    time = (By.XPATH,"//span[.='05:30 PM']")

    def __init__(self,driver):
        super().__init__(driver)

    def click_city(self):
        self.click(self.city)

    def click_select_city(self,city):
        # self.click(self.cross)
        self.enter_text(self.city,city)
        self.click(self.select_city)

    def select_speciality(self):
        self.click(self.speciality)

    def click_gender(self):
        self.click(self.gender)
        self.click(self.female)

    def click_experience(self):
        self.click(self.experience)
        self.click(self.years_of_experience)

    def click_booking(self):
        self.click(self.booking)

    def select_date_and_time(self):
        self.click(self.day)
        self.click(self.time)



