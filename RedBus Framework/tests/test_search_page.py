from pages.search_page import SearchPage
from pages.booking_page import BookingPage
from config.env import ConfigReader
from time import sleep

def test_search_page(setup_and_teardown):
    driver = setup_and_teardown
    search_page = SearchPage(driver)
    booking_page = BookingPage(driver)
    config = ConfigReader.read_config()
    env = config["qa"]
    base_url = env["base_url"]
    city = env["city"]
    mobile_number = env["mobile_number"]
    state = env["state"]
    name = env["name"]
    age = env["age"]
    search_page.hover_from_input()
    search_page.click_from_input()
    search_page.enter_from_city(city)
    # sleep(2)
    search_page.select_to_city()
    # sleep(3)
    search_page.select_date_of_journey()

    booking_page.select_view_seats()
    booking_page.select_seats()
    booking_page.select_boarding_and_dropping_point()
    booking_page.enter_mobile_number(mobile_number)
    booking_page.select_state(state)
    booking_page.enter_name(name)
    booking_page.enter_age(age)
    booking_page.select_gender()
    sleep(3)
    booking_page.click_free_cancellation()
    booking_page.click_assurance()
    booking_page.click_continue_booking()
    sleep(10)

