from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Learn Python\QUPS\chromedriver_win32\chromedriver.exe")
driver.get("https://evaly.com.bd/")

driver.implicitly_wait(10) #seconds
assert "E-valy" in driver.title

print("Application Title : ",driver.title)
print("Application URL : ", driver.current_url)

# if any ads show & automation closed
if (driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section/div/button")):
    driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section/div/button").click()
    print("Cancel Button click.!")

# Login automation =>
driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[2]/div[1]/div/div[2]/div/button").click()
driver.find_element_by_name("phone").send_keys("01748008121")
driver.find_element_by_name("password").send_keys("ah12345#")

driver.find_element_by_xpath("//body/div[@id='custom-popover']/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
# //*[@id='custom-popover']/div/div/div/form/div[3]/button
# //body/div[@id='custom-popover']/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]

print("Login Done !")


print("Finished !")

# driver.close()
