from locators.locators import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


class Elements:
    def __init__(self, driver):
        self.driver = driver
        # self.r_button = Locators.rb
    

    def radio_button_functionality_check(self):
        rbutton_check = self.driver.find_element_by_xpath(Locators.rb)      
        rbutton_check.click()
        status = rbutton_check.is_selected()
        return status

        
    
    # def click_cleaos. execv()r_click (self):
    #     click_clear = self.driver.find_element_by_xpath(self.click_clear)
    #     click_clear.click()

  
    # def input_full_name_field(self,text):
    #     input_name = self.driver.find_element_by_id(self.input_full_name)
    #     input_name.send_keys(text)
    #     print (input_name.text)

    # def input_email_field(self, email):
    #     input_email = self.driver.find_element_by_id(self.input_email)
    #     input_email.send_keys(email)