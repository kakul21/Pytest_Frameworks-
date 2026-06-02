from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def close_popup(self):
        try:
            from selenium.webdriver.common.action_chains import ActionChains
            ActionChains(self.driver).move_by_offset(0, 0).click().perform()
        except:
            pass

    from_dest = (By.XPATH,"//span[.='From']")
    from_city = (By.XPATH,"(//p[.='Mumbai Chhatrapati Shivaji International Airport'])[1]")
    # from_city = (By.XPATH,"(//div[@class='flex flex-grow items-center']//input)[1]")
    from_airport = (By.XPATH,"(//p[.='Jaipur International Airport'])[1]")
    to_dest = (By.XPATH,"//span[.='To']")
    to_city = (By.XPATH,"(//span[.='GOI'])[2]")
    date = (By.XPATH,"(//button[@class='react-calendar__tile react-calendar__month-view__days__day'])[30]")
    travellers = (By.XPATH,"//p[.='Travellers & Class']")
    no_of_travellers_adult = (By.XPATH,"(//button[@data-testid='3'])[1]")
    select_class = (By.XPATH,"//span[.='Premium Economy']")
    done = (By.XPATH,"//button[.='Done']")
    search_button = (By.XPATH,"//button[.='Search']")

    ## Booking Page
    book_button = (By.XPATH,"//button[.='Book']")
    free_booking_cancellation = (By.XPATH,"//span[@class='shrink-0 inline-flex items-center justify-center w-20 h-20 rounded hover:bg-primary-over border border-primary']")
    confirm_button = (By.XPATH,"(//div[@class='flex gap-10'])[2]")
    passenger1 = (By.XPATH,"(//div[@class='inline-flex shrink-0 group-[.list-start.list-sm]:mt-1 group-[.list-start]:mt-2 flex items-start h-full'])[1]")
    passenger2 = (By.XPATH,"(//div[@class='inline-flex shrink-0 group-[.list-start.list-sm]:mt-1 group-[.list-start]:mt-2 flex items-start h-full'])[2]")
    passenger3 = (By.XPATH,"(//div[@class='inline-flex shrink-0 group-[.list-start.list-sm]:mt-1 group-[.list-start]:mt-2 flex items-start h-full'])[3]")
    confirm = (By.XPATH,"//button[.='Confirm']")
    seat1 = (By.XPATH,"(//img[@class='cursor-pointer'])[34]")
    seat2 = (By.XPATH,"(//img[@class='cursor-pointer'])[31]")
    seat3 = (By.XPATH,"(//img[@class='cursor-pointer'])[14]")
    continue_to_pay = (By.XPATH,"//button[.='Continue To Pay']")

    def from_destination(self):
        self.click(self.from_dest)

    def select_from_city(self):
        self.click(self.from_city)
        # self.enter_text(self.from_city,city)
        # self.click(self.from_airport)

    def to_destination(self):
        self.click(self.to_dest)

    def select_to_city(self):
        self.click(self.to_city)

    def select_date(self):
        self.click(self.date)

    def travellers_click(self):
        self.click(self.travellers)
        self.click(self.no_of_travellers_adult)
        self.click(self.select_class)
        self.click(self.done)

    def click_search(self):
        self.click(self.search_button)

    ## Booking Page

    def click_book(self):
        self.click(self.book_button)

    def select_free_booking_cancellation(self):
        self.hover(self.free_booking_cancellation)
        self.click(self.free_booking_cancellation)

    def passenger_click(self):
        self.hover(self.passenger1)
        self.click(self.passenger1)
        self.click(self.confirm)
        self.click(self.passenger2)
        self.click(self.confirm)
        self.click(self.passenger3)
        self.click(self.confirm)

    def confirm_seat(self):
        self.click(self.seat1)
        self.click(self.seat2)
        self.click(self.seat3)

    def confirm_booking(self):
        self.click(self.confirm_button)

    def click_pay(self):
        self.click(self.continue_to_pay)













