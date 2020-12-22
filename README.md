# playwright_stealth

Transplanted from [puppeteer-extra-plugin-stealth](https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth), **Not perfect**.

## Install

```
$ pip install playwright-stealth
```

## Usage

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
```

## Test results

### playwright without stealth

<table class="image">
<tr>
  <td><figure class="image"><a href="https://github.com/ASAS1314/pyppeteer_stealth/images/example1.png"><img src="https://github.com/ASAS1314/pyppeteer_stealth/images/example1.png"></a><figcaption>headless</figcaption></figure></td>
</tr>
</table>

### playwright with stealth

<table class="image">
<tr>
  <td><figure class="image"><a href="https://github.com/ASAS1314/pyppeteer_stealth/images/example.png"><img src="https://github.com/ASAS1314/pyppeteer_stealth/images/example.png"></a><figcaption>headless</figcaption></figure></td>
</tr>
</table>
