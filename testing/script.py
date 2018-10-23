from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://smallpdf.com/pdf-to-word")
button = driver.find_element_by_id('buttonID')
button.click()
