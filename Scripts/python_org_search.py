from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../Drivers/chromedriver.exe")
driver.get("http://www.python.org")
assert "Python" in driver.title

driver.quit()
