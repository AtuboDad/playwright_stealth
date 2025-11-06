from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync


#executablePath = 'C:\\Google\\Chrome\\Application\\chrome.exe'
ipAndPort = '221.1.90.67:9000'
args = [
    '--no-sandbox',
    '--disable-infobars',
    '--lang=zh-CN',
    '--start-maximized',
    '--window-position=0,0',
    # '--proxy-server=http=' + ipAndPort
]

ignoreDefaultArgs = ['--enable-automation']
headless = False

with sync_playwright() as p:
    browser = p.chromium.launch(
        args=args,
        ignore_default_args=ignoreDefaultArgs,
        headless=headless
    )
    page = browser.new_page()
    page.goto('https://bot.sannysoft.com/')

    webdriver_flag = page.evaluate('''() => {
                    return window.navigator.webdriver
                }''')

    # return None
    print(f'window navigator webdriver value: {webdriver_flag}')

    page.screenshot(path=f'example_without_stealth_chrome.png', full_page=True)
    input('Press any key to continue to firefox...')

with sync_playwright() as p:
    browser = p.firefox.launch(
        args=args,
        headless=headless,
    )
    page = browser.new_page()
    page.goto('https://bot.sannysoft.com/')
    webdriver_flag = page.evaluate('''() => {
                    return window.navigator.webdriver
                }''')
    print(f'window navigator webdriver value: {webdriver_flag}')
    page.screenshot(path=f'example_without_stealth_firefox.png', full_page=True)
    input('Press any key to exit...')
