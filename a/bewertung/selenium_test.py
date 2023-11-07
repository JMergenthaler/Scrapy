from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pytz
import re

driver = webdriver.Chrome()



pattern= r'^(.*?\.[0-9]{3})'
neues= datetime.now(pytz.utc)
match = re.search(pattern, str(neues))
if match:
    endstring = match.group(1).strip() + "Z"
else:
    endstring = neues

cookie = {
    "name": "OptanonAlertBoxClosed",
    "value": endstring,
    "domain": ".trustpilot.com",
    "path": "/",
    "expire": "Session"
}

driver.get("https://at.trustpilot.com/review/tfbank.at")

driver.add_cookie(cookie)

title = driver.title


driver.implicitly_wait(0.5)

cookies = driver.get_cookies()
print(cookies)

button_selector = 'button_button__T34Lr.button_s__RG308.button_appearance-secondary__VUFHU.button_wide__yRVpn.styles_button__pwkHk'

buttons = driver.find_elements(By.CLASS_NAME, button_selector)
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, button_selector)))
for button in buttons:
    button.click()


driver.quit()