# playwright_stealth

Transplanted from [puppeteer-extra-plugin-stealth](https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth), **Not perfect**.

## Install

```
$ pip install playwright-stealth
```

## Usage
### sync
```python
from playwright import sync_playwright
from playwright_stealth import stealth_sync

playwright = sync_playwright().start()

# Use playwright.chromium, playwright.firefox or playwright.webkit
# Pass headless=False to see the browser UI
executablePath = 'C:\\Google\\Chrome\\Application\\chrome.exe'
browser = playwright.chromium.launch(executablePath=executablePath, headless=True)
page = browser.newPage()
stealth_sync(page)
page.goto("http://www.example.com/")
browser.close()
playwright.stop()
```
### async
```python
# -*- coding: utf-8 -*-
import asyncio
from playwright import async_playwright
from playwright_stealth import stealth_async


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


async def run(playwright):
    executablePath = 'C:\\Google\\Chrome\\Application\\chrome.exe'
    browser = await playwright.chromium.launch(executablePath=executablePath, headless=True)
    page = await browser.newPage()
    await stealth_async(page)
    await page.goto("http://www.example.com/")

    await browser.close()
    await playwright.stop()


asyncio.get_event_loop().run_until_complete(main())
```

## Test results

### playwright without stealth

![playwright without stealth](https://github.com/ASAS1314/playwright_stealth/blob/main/images/example.png)

### playwright with stealth

![playwright with stealth](https://github.com/ASAS1314/playwright_stealth/blob/main/images/example1.png)
