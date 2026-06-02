from pages.login_page import LoginPage
from config.env import ConfigReader
from time import sleep

def test_login_page(setup_and_teardown):
    driver = setup_and_teardown
    login_page = LoginPage(driver)
    config = ConfigReader.read_config()
    env = config["qa"]
    base_url = env["base_url"]
    USERNAME = env["mobile_number"]
    PASSWORD = env["password"]

    driver.get(base_url)
    login_page.click_login()
    # sleep(5)
    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()


