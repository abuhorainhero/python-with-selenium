from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Learn Python\QUPS\chromedriver_win32\chromedriver.exe")

driver.get("https://www.linkedin.com/in/abuhorain/")
print(driver.title)
driver.get("https://www.facebook.com/mdabuhorain")
print(driver.title)
time.sleep(5)

driver.back()
time.sleep(5)

print(driver.title)

driver.forward()
time.sleep(5)

print(driver.title)


driver.quit()