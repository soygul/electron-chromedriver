# https://sites.google.com/a/chromium.org/chromedriver/getting-started

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

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver_path = "./chromedriver"
electron_path = "/Users/teo/dev/sc-ui/dist/AppGate XDP-darwin-x64/AppGate XDP.app/Contents/MacOS/Electron"

opts = Options()
opts.binary_location = electron_path
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opts)

time.sleep(4)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(4)  # Let the user actually see something!
driver.quit()
