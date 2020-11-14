from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://gmail.com/")
sleep(5)
driver.find_element_by_id('identifierId').send_keys("emailreservagv@gmail.com")
driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
# print(driver.current_url)
# driver.quit()
