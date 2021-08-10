from selenium import webdriver

# from selenium.webdriver.common.keys import keys

# driver = webdriver.Chrome(executable_path="C:\Learn Python\QUPS\chromedriver_win32\chromedriver.exe")

# driver = webdriver.Firefox(executable_path="C:\Learn Python\QUPS\geckodriver-v0.29.1-win64\geckodriver.exe")

driver = webdriver.Ie(executable_path="C:\Learn Python\QUPS\IEDriverServer_x64_.3.150.2\IEDriverServer.exe")

driver.get("https://abuhorain.netlify.app")

print("Application Title ", driver.title)  # Title of the a page
print("Application url ", driver.current_url)  # current_url of the a page

driver.close()
