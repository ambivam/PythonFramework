from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("---------------------------Setup---------------------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    yield
    print("---------------------------Teardown---------------------------")
    driver.quit()


def test_google_title(init_driver):
    assert driver.title == "Google"

def test_google_url(init_driver):
    assert driver.current_url == "https://www.google.com1/?gws_rd=ssl"

@pytest.mark.usefixtures("init_driver")
def test_google_title2():
    assert driver.title == "Google"

@pytest.mark.usefixtures("init_driver")
def test_google_url2():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"


