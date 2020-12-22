from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
# Step 1) Open Firefox 
browser = webdriver.Firefox()

# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")

# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("u_0_b")
username.send_keys("guilhermeviegas1993@gmail.com")
password.send_keys("LetsChange13")

# Step 4) Click Login
submit.click()

time.sleep(3)

minding = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div")

time.sleep(2)

minding.send_keys(" ")

time.sleep(3)
msg = "123456 Oi, eu sou um robô :)"
minding.send_keys(msg)
