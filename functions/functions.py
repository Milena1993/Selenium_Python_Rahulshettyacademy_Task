from locators.locators import LocatorsPath
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Elements:


    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        driver = self.driver
        get_title = driver.title
        current_url = driver.current_url
        return get_title, current_url

    def radio_button_functionality_check(self):
        radio_button_check = self.driver.find_element_by_xpath(LocatorsPath.radion_button)      
        radio_button_check.click()
        status = radio_button_check.is_selected()
        return status

    def suggestion_class_input_field(self, text_input):
        input_field = self.driver.find_element_by_id(LocatorsPath.name_input_field)
        input_field.send_keys(text_input)
        suggested_list = self.driver.find_elements_by_xpath(LocatorsPath.suggested_list)
        for list_item in suggested_list:
            if list_item.text == "Armenia":
                list_item.click()
                return input_field.get_attribute("value")

                  
    def dropdown_element_functionality_check(self):
        dropdown_element_check = self.driver.find_element_by_id(LocatorsPath.dropdown_element)
        drp = Select(dropdown_element_check)
        drp.select_by_visible_text(LocatorsPath.dropdown_option1)
        return drp.first_selected_option.get_attribute("value")
              
    def checkbox_elements_functionality_check(self):
        checkbox_element_1_check = self.driver.find_element_by_id(LocatorsPath.checkbox_element_1)
        checkbox_element_1_check.click()
        checkbox_element_2_check = self.driver.find_element_by_id(LocatorsPath.checkbox_element_2)
        checkbox_element_2_check.click()
        status_checkbox_element1 = checkbox_element_1_check.is_selected()
        status_checkbox_element2 = checkbox_element_2_check.is_selected()
        return status_checkbox_element1, status_checkbox_element2, checkbox_element_1_check.get_attribute("value"), checkbox_element_2_check.get_attribute("value")
        
    def open_window_functiionality_check(self):
        open_window_button_check = self.driver.find_element_by_id(LocatorsPath.open_window_button)
        open_window_button_check.click()
        print(self.driver.current_window_handle)
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy":
                return self.driver.title
            self.driver.close()
                     
    def open_tab_functiionality_check(self):
        open_tab_button_check = self.driver.find_element_by_id(LocatorsPath.open_tab_button)
        open_tab_button_check.click()
        handles_tab = self.driver.window_handles
        for handle in handles_tab:
            self.driver.switch_to.window(handle)
            if self.driver.title == "Rahul Shetty Academy":
                return self.driver.title
            self.driver.close()
                
    def alert_input_field_functiionality_check_accept(self, input_name):
        alert_button_check = self.driver.find_element_by_id(LocatorsPath.alert_button_input_field)
        alert_button_check.send_keys(input_name)
        alert_button_click = self.driver.find_element_by_id(LocatorsPath.alert_button)
        alert_button_click.click()
        obj = self.driver.switch_to.alert
        msg = obj.text
        obj.accept()
        if msg == "Hello Milena, share this practice page and share your knowledge":
            return msg
    
    def alert_input_field_functiionality_check_dismiss(self, input_name):
        alert_button_check = self.driver.find_element_by_id(LocatorsPath.alert_button_input_field)
        alert_button_check.send_keys(input_name)
        alert_button_click = self.driver.find_element_by_id(LocatorsPath.confirm_button)
        alert_button_click.click()
        obj = self.driver.switch_to.alert
        msg = obj.text
        obj.dismiss()
        if msg == "Hello Milena, Are you sure you want to confirm?":
            return msg
        
    def mouse_hover_functionality_check(self):
        mouse_hover_button = self.driver.find_element_by_xpath(LocatorsPath.mouse_hover_button)
        top_button = self.driver.find_element_by_css_selector(LocatorsPath.mouse_hover_top_button)
        realod_button = self.driver.find_element_by_css_selector(LocatorsPath.mouse_hover_reload_button)
        actions = ActionChains(self.driver)
        actions.move_to_element(mouse_hover_button).move_to_element(top_button).move_to_element(realod_button).click().perform()

    def table_scrolling_functionality_check(self):
        table_Scrolling = self.driver.find_element_by_xpath(LocatorsPath.table_scroll) 
        self.driver.execute_script("arguments[0].scrollTop = 200", table_Scrolling)

    def show_button_functionality_check(self, show_input):
        show_button_check = self.driver.find_element_by_id(LocatorsPath.show_button)
        show_button_check.click()
        displayed_element = self.driver.find_element_by_id(LocatorsPath.displayed_element)
        displayed_element.send_keys(show_input)
        return  displayed_element.get_attribute("value")

    def hide_button_functionality_check(self):
        hide_button_check = self.driver.find_element_by_id(LocatorsPath.hide_button)
        hide_button_check.click()
        displayed_element = self.driver.find_element_by_id(LocatorsPath.displayed_element)
        status =  displayed_element.is_displayed()
        return status

    def frame_functionality_check(self):
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        self.driver.switch_to.frame(LocatorsPath.frame)
        courses_button = self.driver.find_element_by_link_text(LocatorsPath.courses_button)
        courses_button.click()
        javascript_button = self.driver.find_element_by_xpath(LocatorsPath.javascript_button)
        status = javascript_button.is_displayed()
        return status
        