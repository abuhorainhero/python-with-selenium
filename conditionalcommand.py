from selenium import  webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Learn Python\QUPS\chromedriver_win32\chromedriver.exe")
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

user_ele = driver.find_element_by_name("firstname")
print(user_ele.is_displayed())  # Return true/flase based of element status
print(user_ele.is_enabled())  # Return true/flase based of element status

pass_ele = driver.find_element_by_name("lastname")
print(pass_ele.is_displayed())  # Return true/flase based of element status
print(pass_ele.is_enabled())  # Return true/flase based of element status

user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")

roundtrip_radio = driver.find_element_by_css_selector("input[value=Male]")
print("Radio Male ",roundtrip_radio.is_selected())

roundtrip_radio_2 = driver.find_element_by_css_selector("input[value=Female]")
print("Radio Female ",roundtrip_radio_2.is_selected())

driver.close()