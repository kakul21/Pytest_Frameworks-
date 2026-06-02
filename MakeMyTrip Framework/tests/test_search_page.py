from pages.search_page import SearchPage
from config.env import ConfigReader
from time import sleep

def test_search_page(setup_and_teardown):
    driver = setup_and_teardown
    search_page = SearchPage(driver)
    config = ConfigReader.read_config()
    env = config["qa"]
    base_url = env["base_url"]
    # driver.get(base_url)
    search_page.close_popup()
    search_page.click_hotels()
    sleep(5)
    search_page.click_city()
    search_page.enter_city('Goa')
    search_page.check_in_and_out_date()
    search_page.click_apply()
    search_page.click_search()
    sleep(5)
