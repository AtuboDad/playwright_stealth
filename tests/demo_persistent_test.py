import getpass

from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync


chrome_path = 'C:\\Google\\Chrome\\Application\\chrome.exe'
# 当前用户的Chrome缓存路径
user_dir_path = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Google\\Chrome\\User Data"
channel = 'chrome'
headless = False
args = ['--ignore-certificate-errors',
        '--ignore-certificate-errors-spki-list',
        '--disable-blink-features=AutomationControlled',
        '--disable-shm-usage',
        '--disable-infobars',
        '--start-maximized',
        '--window-position=-10,0']


# Use system use's chrome cache folder
with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
                    user_data_dir=user_dir_path,
                    channel=channel,
                    executable_path=chrome_path,
                    args=args,
                    accept_downloads=True,
                    headless=False,
                    bypass_csp=True,
                )

    page = browser.new_page()
    # stealth_sync(page)
    page.goto('https://bot.sannysoft.com/')
    webdriver_flag = page.evaluate('''() => {
                return window.navigator.webdriver
            }''')

    # return False
    print(f'window navigator webdriver value: {webdriver_flag}')
    page.screenshot(path=f'example_with_persistent.png')
