# -*- coding: utf-8 -*-
import json
import os
from dataclasses import dataclass
from typing import Tuple, Optional, Dict

from playwright.async_api import Page as AsyncPage
from playwright.sync_api import Page as SyncPage


def from_file(name) -> str:
    """Read script from ./js directory"""
    filename = os.path.join(os.path.dirname(__file__), "js", name)
    with open(filename, encoding="utf-8") as f:
        return f.read()


SCRIPTS: Dict[str, str] = {
    "chrome_csi": from_file("chrome.csi.js"),
    "chrome_app": from_file("chrome.app.js"),
    "chrome_runtime": from_file("chrome.runtime.js"),
    "chrome_load_times": from_file("chrome.load.times.js"),
    "chrome_hairline": from_file("chrome.hairline.js"),
    "generate_magic_arrays": from_file("generate.magic.arrays.js"),
    "iframe_content_window": from_file("iframe.contentWindow.js"),
    "media_codecs": from_file("media.codecs.js"),
    "navigator_vendor": from_file("navigator.vendor.js"),
    "navigator_plugins": from_file("navigator.plugins.js"),
    "navigator_permissions": from_file("navigator.permissions.js"),
    "navigator_languages": from_file("navigator.languages.js"),
    "navigator_platform": from_file("navigator.platform.js"),
    "navigator_user_agent": from_file("navigator.userAgent.js"),
    "navigator_user_agent_data": from_file("navigator.userAgentData.js"),
    "navigator_hardware_concurrency": from_file("navigator.hardwareConcurrency.js"),
    "outerdimensions": from_file("window.outerdimensions.js"),
    "utils": from_file("utils.js"),
    "webdriver": from_file("navigator.webdriver.js"),
    "webgl_vendor": from_file("webgl.vendor.js"),
}


@dataclass
class StealthConfig:
    """
    Playwright stealth configuration that applies stealth strategies to playwright page objects.
    The stealth strategies are contained in ./js package and are basic javascript scripts that are executed
    on every page.goto() called.
    Note:
        All init scripts are combined by playwright into one script and then executed this means
        the scripts should not have conflicting constants/variables etc. !
        This also means scripts can be extended by overriding enabled_scripts generator:
        ```
        @property
        def enabled_scripts():
            yield 'console.log("first script")'
            yield from super().enabled_scripts()
            yield 'console.log("last script")'
        ```
    """

    # load script options
    webdriver: bool = True
    webgl_vendor: bool = True
    chrome_app: bool = True
    chrome_csi: bool = True
    chrome_load_times: bool = True
    chrome_runtime: bool = True
    iframe_content_window: bool = True
    media_codecs: bool = True
    navigator_hardware_concurrency: int = 4
    navigator_languages: bool = True
    navigator_permissions: bool = True
    navigator_platform: bool = True
    navigator_plugins: bool = True
    navigator_user_agent: bool = True
    navigator_user_agent_data: bool = True
    navigator_vendor: bool = True
    outerdimensions: bool = True
    hairline: bool = True

    # options
    vendor: str = "Google Inc. (Apple)"
    renderer: str = (
        "ANGLE (Apple, ANGLE Metal Renderer: Apple M2 Max, Unspecified Version)"
    )
    nav_vendor: str = "Google Inc."
    nav_user_agent: str = None
    nav_platform: str = None
    languages: Tuple[str] = ("en-US", "en")
    runOnInsecureOrigins: Optional[bool] = None

    @property
    def enabled_scripts(self):
        opts = json.dumps(
            {
                "webgl_vendor": self.vendor,
                "webgl_renderer": self.renderer,
                "navigator_vendor": self.nav_vendor,
                "navigator_platform": self.nav_platform,
                "navigator_user_agent": self.nav_user_agent,
                "navigator_user_agent_data": self.navigator_user_agent_data,
                "languages": list(self.languages),
                "runOnInsecureOrigins": self.runOnInsecureOrigins,
            }
        )

        # defined options constant
        yield f"window.opts = {opts}; console.log('opts defined:', window.opts);"
        # init utils and generate_magic_arrays helper
        yield SCRIPTS["utils"]
        yield SCRIPTS["generate_magic_arrays"]

        script_keys = [
            "chrome_app",
            "chrome_csi",
            "chrome_hairline",
            "chrome_load_times",
            "chrome_runtime",
            "iframe_content_window",
            "media_codecs",
            "navigator_languages",
            "navigator_permissions",
            "navigator_platform",
            "navigator_plugins",
            "navigator_user_agent",
            "navigator_user_agent_data",
            "navigator_vendor",
            "webdriver",
            "outerdimensions",
            "webgl_vendor",
        ]

        for key in script_keys:
            yield f"{SCRIPTS[key]}; console.log('Script {key} executed with opts:', window.opts);"


def stealth_sync(page: SyncPage, config: StealthConfig = None):
    """teaches synchronous playwright Page to be stealthy like a ninja!"""
    for script in (config or StealthConfig()).enabled_scripts:
        page.add_init_script(script)


async def stealth_async(page: AsyncPage, config: StealthConfig = None):
    """teaches asynchronous playwright Page to be stealthy like a ninja!"""
    for script in (config or StealthConfig()).enabled_scripts:
        await page.add_init_script(script)
