from selenium import webdriver

PROXY = "127.0.0.1:22999" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

chrome = webdriver.Chrome(options=chrome_options)
chrome.get("http://whatismyipaddress.com")


