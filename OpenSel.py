import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.log.level = "trace"

#code to drop magnet link in deluge
browser = webdriver.Firefox(options = opts)
browser.get('http://localhost:8112/')

print("opening web-ui")
time.sleep(2)

#trying login if necessary
try:
    loginText = browser.find_element_by_id("_password")
    print("login required")
    loginText.send_keys("deluge")
    loginBtn = browser.find_element_by_xpath("//button[contains(text(),'Login')]")
    loginBtn.click()
except:
    print("no login !")

time.sleep(2)

AddBtn1 = browser.find_element_by_class_name("icon-add")
AddBtn1.click()

UrlBtn = browser.find_element_by_class_name("icon-add-url")
UrlBtn.click()

UrlTxt = browser.find_element_by_id("url")
UrlTxt.send_keys("breh")

AddBtns = browser.find_elements_by_xpath("//em/button[contains(text(), 'Add')]")
AddBtns[2].click()
AddBtns[1].click()