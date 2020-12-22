from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import yaml


with open('PY/helper/globalsource.yaml', 'r') as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)
f.close()

class NewPost:
    def __init__(self, user, passwd):
        self.browser  = webdriver.Firefox()
        self.browser.get("http://www.facebook.com")
        self.user = user
        self.passwd = passwd
        self.username = self.browser.find_element_by_id("email")
        self.password = self.browser.find_element_by_id("pass")
        self.submit   = self.browser.find_element_by_id("u_0_b")
        
    def insertCredential(self):
        self.username.send_keys(self.user)
        self.password.send_keys(self.passwd)
        self.submit.click()
        time.sleep(3)

    def sendMsg(self, msg):
        self.minding = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div")
        time.sleep(2)
        self.minding.send_keys(" ")
        time.sleep(3)
        self.minding.send_keys(msg)

    def run(self, msg):
        self.insertCredential()
        self.sendMsg(msg)
        time.sleep(3)
        self.browser.quit()

fb = NewPost(
    user = cred["email"], 
    passwd = cred["secret"]
)

fb.run(msg = " Oi, eu sou um robô :)")

