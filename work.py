from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
import pickle

HEADLESS = False
PROXY = "127.0.0.1:22999"
# myToken = '2XHDdTw4XP6SksUqJCC45GAE5Lv3rYqD'

def get_browser():
    chrome_options = Options()
    if HEADLESS:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(executable_path= r"/root/facebook_visit/chromedriver" ,options=chrome_options)
    return browser  

if __name__ == '__main__':
    browser = get_browser()
    browser.get('http://lumtest.com/myip.json')
    print(browser.find_element_by_xpath("/html/body").text)
    sleep(2)
    print("sucess")

