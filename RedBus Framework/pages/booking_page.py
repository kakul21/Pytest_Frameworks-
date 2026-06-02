from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BookingPage(BasePage):

    View_seats = (By.XPATH, "(//button[contains(text(),'View seats')])[1]")
    seat = (By.XPATH, "//span[@id='UF']")
    boarding_and_dropping_point = (By.XPATH, "//button[@aria-label='Select boarding & dropping points']")
    boarding_point = (By.XPATH, "(//div[@class='radioContainer___db0bbf'])[1]")
    dropping_point = (By.XPATH, "(//div[@class='radioContainer___db0bbf'])[9]")
    mobile_number = (By.XPATH, "//input[@id='0_6']")
    input_state_field = (By.XPATH, "//div[@class='inputBox___5e7fb8   ']")
    search_field = (By.XPATH, "//input[@placeholder='Search for state']")
    choose_state = (By.XPATH, "(//label[@class='customRadio___b65f5d customRadio___b65f5d'])[6]")
    name = (By.XPATH, "//input[@id='0_4']")
    age = (By.XPATH, "//input[@id='0_1']")
    gender = (By.XPATH, "(//span[@class='toggleCircle___57beb9   '])[2]")
    Free_cancellation = (By.XPATH, "(//label[@class='customRadio___b65f5d customRadio___b65f5d'])[1]")
    Assurance = (By.XPATH, "(//label[@class='customRadio___b65f5d customRadio___b65f5d'])[5]")
    continue_booking = (By.XPATH, "//button[.='Continue booking']")

    def __init__(self, driver):
        super().__init__(driver)

    def select_view_seats(self):
        self.click(self.View_seats)

    def select_seats(self):
        self.click(self.seat)

    def select_boarding_and_dropping_point(self):
        self.click(self.boarding_and_dropping_point)
        self.click(self.boarding_point)
        self.click(self.dropping_point)

    def enter_mobile_number(self,mobile_number):
        self.click(self.mobile_number)
        self.enter_text(self.mobile_number,mobile_number)

    def select_state(self,state):
        self.click(self.input_state_field)
        self.click(self.search_field)
        self.enter_text(self.search_field,state)
        self.click(self.choose_state)

    def enter_name(self,name):
        self.click(self.name)
        self.enter_text(self.name,name)

    def enter_age(self,age):
        self.click(self.age)
        self.enter_text(self.age,age)

    def select_gender(self):
        self.click(self.gender)

    def click_free_cancellation(self):
        self.click(self.Free_cancellation)

    def click_assurance(self):
        self.click(self.Assurance)

    def click_continue_booking(self):
        self.click(self.continue_booking)