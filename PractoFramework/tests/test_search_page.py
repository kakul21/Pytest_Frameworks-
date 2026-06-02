from pages.search_page import SearchPage
from config.env import ConfigReader
from time import sleep

def test_search_page(setup_and_teardown):
    driver = setup_and_teardown
    search_page = SearchPage(driver)
    config = ConfigReader.read_config()
    env = config["qa"]
    base_url = env["base_url"]
    CITY = env["city"]

    # driver.get(base_url)
    search_page.click_city()
    sleep(3)
    search_page.click_select_city(CITY)
    # sleep(5)
    search_page.select_speciality()
    sleep(3)
    search_page.click_gender()
    sleep(3)
    search_page.click_experience()
    sleep(3)
    search_page.click_booking()
    sleep(3)
    search_page.select_date_and_time()
    sleep(5)