from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Learn Python\QUPS\chromedriver_win32\chromedriver.exe")
driver.get("https://abuhorain.netlify.app")

print("Application Title : ", driver.title)
print("Application URL : ", driver.current_url)

driver.find_element_by_xpath("//*[@id='responsive-navbar-nav']/div[1]/a[6]/button").click()

time.sleep(5)

# driver.close()     # Closed Currently focussed browser
driver.quit()        # Closed All browsers 
