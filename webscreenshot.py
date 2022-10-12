# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# @0xDanielLopez 2022

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException

from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

import time
import sys, os
from tld import get_tld

# Config
timeout_screenshot = 6	# Time waiting until screenshot

#Colours
RED = '\033[91m'
ENDC = '\033[0m'
GREEN = '\033[1;32m'
WHITE = '\033[1m'
BOLD = '\033[01m'
BLUE = '\033[94m'
ORANGE = '\033[38;5;202m'

# Browser configuration
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,950")
chrome_options.add_argument("--incognito")

# Selenium 3
driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=chrome_options)

# Selenium 4
#driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chrome_options)

driver.set_page_load_timeout(timeout_screenshot)

# Get the URLs
with open('urls.dat', 'r') as f:
	urls = f.readlines()
urls = [x.strip() for x in urls]

# Configure output directory
screenshot_path = ("output")
if not os.path.exists(screenshot_path):
	os.makedirs(screenshot_path)

# Starts
count=1

print(40*"=")
print("[+] Starting ...")
for url in urls:
	aux_tld = get_tld(url, as_object=True)
	print("\t{} - {}".format(count,url))

	new_screenshot =('%s/%s_%s-%s.png') % (screenshot_path,str(count),str(aux_tld.domain),str(aux_tld.suffix))
	driver.get(url)

	screenshot = driver.save_screenshot(new_screenshot)
	count=count+1

print(40*"=")
driver.quit()
