import pytest
from selenium import webdriver
from config.env import ConfigReader

@pytest.fixture(scope="session")
def setup_and_teardown():
    config = ConfigReader.read_config()
    env = config["qa"]
    base_url = env["base_url"]
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()

