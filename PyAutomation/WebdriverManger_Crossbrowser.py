from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browser = "chrome1"
driver = ''

if(browser == "chrome"):
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print("plkease pass the cotrrect browser name "+browser)
    raise Exception("Driver is not available")

driver.implicitly_wait(5)

driver.get("https://app.hubspot.com/login")

time.sleep(20)

driver.find_element(By.ID,"username").send_keys("rajanikanth.bathula@gmail.com")

driver.find_element(By.ID,"password").send_keys("Mouritechno#1")
driver.find_element(By.ID,"loginBtn").click()

time.sleep(3)

# driver.quit()