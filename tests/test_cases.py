from selenium import webdriver
from base_page.base_page import Base
from functions.functions import Elements
from locators.locators import Locators
from time import sleep
import pytest


@pytest.mark.usefixtures('set_up')
class TestPositive(Base):

#Assert that radio_button is selected 
    def test_radio_button_functionality_check(self):
        # driver = self.driver
        actual_result = Elements.radio_button_functionality_check(self)
        # actual_result= bool(actual_result)
        expected_result = True
        # self.assertTrue(actual_result.isSelected())
        # # print(type(expected_result))
        assert  actual_result == expected_result
        #actual_result.is_selected() == True
        # print(actual_result)