from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')
#wait for page to load
#time.sleep(5)

assert 'Django' in browser.title
