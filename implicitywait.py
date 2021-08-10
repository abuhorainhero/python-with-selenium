from selenium import  webdriver

driver = webdriver.Chrome(executable_path="C:\Learn Python\QUPS\chromedriver_win32\chromedriver.exe")
driver.get("https://evaly.com.bd/")

driver.implicitly_wait(10)    # seconds
assert "E-valy" in driver.title

if (driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section/div/button")):
    driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section/div/button").click()
    print("Cancel Button click.!")

driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[2]/div[1]/div/div[2]/div/button").click()
print("Button Click.!")

driver.find_element_by_name("phone").send_keys("01748008121")
driver.find_element_by_name("password").send_keys("ah12345#")

# driver.find_element_by_xpath("//*[@id='custom-popover']/div/div/div/form/div[3]/button").click()
driver.find_element_by_css_selector("#custom-popover > div > div > div > form > div.p-4.text-center > button").click()

print("Finished !")
