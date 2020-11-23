import bs4
import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get('https://www.instagram.com');
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button').click()
username_box=driver.find_element_by_name('username')
username_box.send_keys("YOUR USERNAME")
time.sleep(2)
password_box=driver.find_element_by_name('password')

password_box.send_keys("PASSWORD")
time.sleep(3)
login_box=driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button')
login_box.click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button').click()
time.sleep(10)
for i in range(0,460):
    driver.get('https://www.instagram.com/memesrut1/feed')
    time.sleep(10)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/div[1]/div/article[1]/div[1]/button/div/div").click()
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/button[1]').click()
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button[1]').click()
    time.sleep(10)
    
