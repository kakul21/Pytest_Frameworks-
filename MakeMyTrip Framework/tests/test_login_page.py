from pages.login_page import LoginPage
from config.env import ConfigReader
from time import sleep

def test_login_page(setup_and_teardown):
    driver = setup_and_teardown
    login_page = LoginPage(driver)
    config = ConfigReader.read_config()
    env = config["qa"]
    base_url = env["base_url"]
    EMAIL = env["email"]
    PASSWORD = env["password"]
    driver.get(base_url)
    # sleep(3)
    login_page.click_login_button()
    login_page.click_login()
    sleep(3)
    login_page.click_google_signin()
    sleep(5)
    login_page.switch_to_google_window()
    login_page.enter_google_email(EMAIL)
    # sleep(3)
    login_page.click_email_next()
    # sleep(4)
    login_page.enter_google_password(PASSWORD)
    login_page.click_password_next()
    sleep(7)
    driver.switch_to.window(login_page.main_window)
    sleep(15)
    login_page.close_popup()
    sleep(5)


