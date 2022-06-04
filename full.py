from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome(executable_path = "chromedriver/chromedriver.exe")
driver.get(url="https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

Radiobutton
radio_button =driver.find_element_by_xpath('//*[@id="radio-btn-example"]/fieldset/label[1]/input').click() #Clicks the radio button
radio_button =driver.find_element_by_css_selector("input[value='radio1']").click()


# button = driver.find_element_by_css_selector('label[for=radio1]')
status = driver.find_element_by_xpath('//*[@id="radio-btn-example"]/fieldset/label[1]/input').is_selected()
print(status)

#Suggession Class Example

# input_field =driver.find_element_by_xpath('//*[@id="autocomplete"]')
input_field =driver.find_element_by_id("autocomplete")
input_field.send_keys("Milena")



# #dropdown
dropdown_element = driver.find_element_by_id('dropdown-class-example')
drp = Select(dropdown_element)
drp.select_by_visible_text('Option1')
all_options = drp.options

for option in all_options:
    print(option.text)


# #checkbox
# checkbox_element1 = driver.find_element_by_id('checkBoxOption1').click()
# checkbox_element2 = driver.find_element_by_id('checkBoxOption2').click()
# status_checkbox_elent1 = driver.find_element_by_id('checkBoxOption1').is_displayed()
# print(status_checkbox_elent1)


# # driver.close()


# #open window


# # open_window_button = driver.find_element_by_id('openwindow').click()
# # print(driver.current_window_handle)

# # handles = driver.window_handles  #return all the handle values of the opened browser windows

# # for handle in handles:
# #     driver.switch_to.window(handle)
# #     print(driver.title)
# #     if driver.title == "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy":
# #         driver.close()

# time.sleep(5)
# #open tab 
# open_tab_button = driver.find_element_by_id('opentab').click()
# handles_tab = driver.window_handles
# for handle in handles_tab:
#     driver.switch_to.window(handle)
#     print(driver.title)
#     if driver.title == "Rahul Shetty Academy":
#         driver.close()


# #alert
# alert_input_field = driver.find_element_by_id('name').send_keys("Milena")
# alert_button_click = driver.find_element_by_id('alertbtn').click()
# time.sleep(3)
# obj = driver.switch_to.alert
# msg = obj.text
# obj.accept()
# if msg == "Hello Milena, share this practice page and share your knowledge":
#    print("test passed")

# alert_input_field = driver.find_element_by_id('name').send_keys("Milena")
# confirm_button = driver.find_element_by_id('confirmbtn').click()
# time.sleep(3)
# obj = driver.switch_to.alert
# msg = obj.text
# obj.dismiss()
# if msg == "Hello Milena, Are you sure you want to confirm?":
#     print('yes')



# #mousehoveraction

# mouse_hover_button = driver.find_element_by_xpath('//*[@id="mousehover"]')
# top_button = driver.find_element_by_css_selector('.mouse-hover-content > a:nth-child(1)')
# realod_button = driver.find_element_by_css_selector('.mouse-hover-content > a:nth-child(2)')


# actions = ActionChains(driver)
# actions.move_to_element(mouse_hover_button).move_to_element(top_button).move_to_element(realod_button).click().perform()

# #table scrolling

# table = driver.find_element_by_xpath('/html/body/div[3]/div[2]/fieldset[2]/div[1]') 
# driver.execute_script("arguments[0].scrollTop = 200", table)