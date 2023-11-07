from playwright.sync_api import sync_playwright
from datetime import datetime
import pytz
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()
    page = context.new_page()

    pattern= r'^(.*?\.[0-9]{3})'
    neues= datetime.now(pytz.utc)
    match = re.search(pattern, str(neues))
    if match:
        endstring = match.group(1).strip() + "Z"
    else:
        endstring = neues
    
    cookies_to_add = [{
        "name": "OptanonAlertBoxClosed",
        "value": endstring,
        "domain": ".trustpilot.com",
        "path": "/"
        }
    ]

    context.add_cookies(cookies_to_add)
    page.goto('https://at.trustpilot.com/review/tfbank.at')
    button_selector = '.button_button__T34Lr.button_s__RG308.button_appearance-secondary__VUFHU.button_wide__yRVpn.styles_button__pwkHk'
    buttons = page.query_selector_all(button_selector)
    for button in buttons:
        button.click()
    page.click("button#es")
