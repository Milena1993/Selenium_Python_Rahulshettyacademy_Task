from typing_extensions import Self
from selenium import webdriver
from base_page.base_page import Base
from functions.functions import Elements
from locators.locators import LocatorsPath
from time import sleep
import pytest


@pytest.mark.usefixtures('set_up')
class TestPositive(Base):

# Assert that  page is opened
    def test_title(self):
        actual_result = Elements.get_page_title(self)
        expected_result = ("Practice Page", "https://www.rahulshettyacademy.com/AutomationPractice/")
        assert actual_result == expected_result
        print(actual_result)
     


# Assert that webelements functionalities are working fine
    def test_web_elements_functionality_check(self):

        driver = self.driver
        elements_check = Elements(driver)
        radio_button_testresult = Elements.radio_button_functionality_check(self)
        assert radio_button_testresult == True

        input_field_testresult = elements_check.suggestion_class_input_field("arm")
        assert input_field_testresult == "Armenia"
        
        dropdown_element_testresult = Elements.dropdown_element_functionality_check(self)
        assert dropdown_element_testresult == "option1"

    
        checkbox_element_testresult = Elements.checkbox_elements_functionality_check(self)
        assert checkbox_element_testresult == (True, True, 'option1', 'option2')

        
        open_window_testresult = Elements.open_window_functiionality_check(self)
        assert open_window_testresult == "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy"
    

    def test_open_tab_functionality_check(self):
        open_tab_testresult = Elements.open_tab_functiionality_check(self)
        assert open_tab_testresult == "Rahul Shetty Academy"
       

    def test_web_elements_functionality_check2(self):
        driver = self.driver
        elements_check = Elements(driver)
        alert_button_accept_test_result= elements_check.alert_input_field_functiionality_check_accept("Milena")
        assert  alert_button_accept_test_result == 'Hello Milena, share this practice page and share your knowledge'

        alert_button_dismiss_test_result = elements_check.alert_input_field_functiionality_check_dismiss("Milena")
        assert  alert_button_dismiss_test_result == "Hello Milena, Are you sure you want to confirm?"

        Elements.mouse_hover_functionality_check(self)
        Elements.table_scrolling_functionality_check(self)
        

        show_button_test_result = Elements.show_button_functionality_check(self, "Milena" )
        assert show_button_test_result == "Milena"

        hide_button_test_result = Elements.hide_button_functionality_check(self)
        assert hide_button_test_result == False

    def test_frame_functionality(self):
        frame_testresult = Elements.frame_functionality_check(self)
        assert frame_testresult == True
    