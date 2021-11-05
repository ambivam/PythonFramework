from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    assert driver.title == "Google"
    driver.quit()

def test_mouritech():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.mouritech.com")
    assert driver.title.lower().find("mouri tech") >= 0
    driver.quit()

def test_microsoft():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.microsoft.com")
    assert driver.title.lower().find("microsoft") >= 0
    driver.quit()

def test_f1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.f1.com")
    assert driver.title.lower().find("formula") >= 0
    driver.quit()