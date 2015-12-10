# https://sites.google.com/a/chromium.org/chromedriver/getting-started

# alternative for not restarting the chromedriver for every test case and continuously use existing instance

# import time
# from selenium import webdriver
# import selenium.webdriver.chrome.service as service
#
# service = service.Service('./chromedriver')
# service.start()
# capabilities = {
#     'chrome.binary': '/Users/teo/dev/sc-ui/dist/AppGate XDP-darwin-x64/AppGate XDP.app/Contents/MacOS/Electron'}
# driver = webdriver.Remote(service.service_url, capabilities)
# driver.get('http://www.google.com/xhtml')
# time.sleep(1)  # Let the user actually see something!
# driver.quit()

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver_path = "./chromedriver"
electron_path = "/Users/teo/dev/sc-ui/dist/AppGate XDP-darwin-x64/AppGate XDP.app/Contents/MacOS/Electron"

opts = Options()
opts.binary_location = electron_path
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opts)
driver.implicitly_wait(15)  # seconds

time.sleep(3)

username = driver.find_element_by_css_selector('#cards > div.cards.style-scope.task-cards > task-card > sign-in > div > div > paper-input:nth-child(3) > paper-input-container > div.input-content.style-scope.paper-input-container #labelAndInputContainer #input')
username.send_keys('teoman.soygul')
password = driver.find_element_by_css_selector('#cards > div.cards.style-scope.task-cards > task-card > sign-in > div > div > paper-input:nth-child(4) > paper-input-container > div.input-content.style-scope.paper-input-container #labelAndInputContainer #input')
password.send_keys(os.environ['PASS'])

time.sleep(2)

connect_button = driver.find_element_by_css_selector('#signInButton')
connect_button.click()

time.sleep(15)  # wait for sign in

menu_button = driver.find_element_by_css_selector('#menuButton')
menu_button.click()
time.sleep(1)
logout_button = driver.find_element_by_css_selector('#contentWrapper > paper-material > paper-menu > div > a:nth-child(3)')
logout_button.click()

time.sleep(3)

menu_button = driver.find_element_by_css_selector('#menuButton')
menu_button.click()
time.sleep(1)
quit_button = driver.find_element_by_css_selector('#contentWrapper > paper-material > paper-menu > div > a:nth-child(4)')
quit_button.click()

time.sleep(2)

driver.quit()
