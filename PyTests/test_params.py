from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHubSpot(BaseTest):
    @pytest.mark.parametrize(
            "username,password",
            [
                ("rajanib.in@mouritech.com","Mouritechno#1"),
                ("rajanib2.in@mouritech.com", "Mouritechno#12")
            ]
                              )
    def test_login(self,username,password):
        """
        This method is used to login into tricentis web demo app
        :param username:
        :param password:
        :return:
        """
        self.driver.get("http://demowebshop.tricentis.com/login")
        self.driver.find_element_by_xpath('//*[@id="Email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="Password"]').send_keys(password)
        self.driver.find_element_by_xpath('//body/div[4]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[5]/input[1]').click()


