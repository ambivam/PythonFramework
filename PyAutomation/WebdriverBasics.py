from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://phptravels.com/demo/")
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/header/div/nav/div[2]/span").click()
time.sleep(2)

options = driver.find_elements(By.XPATH,'/html/body/header/div/nav/div[2]/div/a')
print("Options length is "+ str(len(options)))
for opt in options:
    print(opt.text)
    if opt.text.strip() == 'Integrations':
        opt.click()
        break
print(len(options))


print(driver.title)

# #contents

