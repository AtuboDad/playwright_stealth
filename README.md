# playwright_stealth

Transplanted from [puppeteer-extra-plugin-stealth](https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth), **Not perfect**.

## Install

```
$ pip install playwright-stealth
```

## Usage

Default stealth
### sync
```python
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        stealth_sync(page)
        page.goto('https://bot.sannysoft.com/')
        page.screenshot(path=f'example-{browser_type.name}.png', full_page=True)
        browser.close()
```

### async
```python
# -*- coding: utf-8 -*-
import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch(headless=False)
            page = await browser.new_page()
            await stealth_async(page)
            await page.goto('https://bot.sannysoft.com/')
            await page.screenshot(path=f'example-{browser_type.name}.png', full_page=True)
            await browser.close()

asyncio.run(main())
```

Desired stealth argument (as a mobile device)
### sync 
```python
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync, StealthConfig

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch(headless=False)
        context = browser.new_context(**p.devices["Pixel 7"])
        page = context.new_page()
        # Setting desired values for navigator properties
        stealth_config = StealthConfig(
            languages = ['en-US', 'en'],
            navigator_plugins = False, # Mimicking real mobile device
            navigator_hardware_concurrency = 8,
            # nav_vendor = "", # Use only if you need to set empty string value to mimicking Firefox browser
            nav_platform= 'Linux armv81',
            vendor = 'Google Inc. (Qualcomm)',
            renderer = 'ANGLE (Qualcomm, Adreno (TM) 640, OpenGL ES 3.2)',
        )
        stealth_sync(page, stealth_config)
        page.goto('https://bot.sannysoft.com/')
        page.screenshot(path=f'example-{browser_type.name}.png', full_page=True)
        browser.close()
```

### async
```python
# -*- coding: utf-8 -*-
import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async, StealthConfig

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch(headless=False)
            context = await browser.new_context(**p.devices["Pixel 7"])
            page = await context.new_page()
            # Setting desired values for navigator properties
            stealth_config = StealthConfig(
                languages = ['en-US', 'en'],
                navigator_plugins = False, # Mimicking real mobile device
                navigator_hardware_concurrency = 8,
                # nav_vendor = "", # Use only if you need to set empty string value to mimicking Firefox browser
                nav_platform= 'Linux armv81',
                vendor = 'Google Inc. (Qualcomm)',
                renderer = 'ANGLE (Qualcomm, Adreno (TM) 640, OpenGL ES 3.2)',
            )
            await stealth_async(page, stealth_config)
            await page.goto('https://bot.sannysoft.com/')
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

asyncio.run(main())
```

## Test results
### Playwright with stealth(no passed argument)
![playwright with stealth](./images/example_with_stealth.png)

### Playwright without stealth
![playwright without stealth](./images/example_without_stealth.png)

### Playwright with stealth(with passed argument) but as a mobile device
*NB: Mobile device have no plugin unlike desktop*
![playwright stealth with specified arguments](./images/example_with_stealth_passed_arguments.png)
