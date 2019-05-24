from selenium import webdriver

browser = webdriver.Firefox(firefox_binary="/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox-bin")
browser.get('http://localhost:8000')


assert 'Django' in browser.title
