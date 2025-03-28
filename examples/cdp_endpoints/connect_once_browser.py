"""
Example demonstrating how to connect to a once-off browser using Chrome DevTools Protocol
and control it using Playwright.
"""

import os
import asyncio
from nstbrowser import NstbrowserClient


def get_cdp_websocket_url():
    api_key = os.environ.get(
        "NSTBROWSER_API_KEY",
        "your_api_key"
    )
    config = {
        "name": "testProfile",
        "platform": "Windows",
        "kernelMilestone": "132",
        "autoClose": False,
        "timedCloseSec": 30,
        "headless": False,
        "incognito": False,
        # "proxy": "http://admin:123456@127.0.0.1:8000",
        "skipProxyChecking": True,
        "fingerprint": {
            "flags": {
                "audio": "Noise",
                "battery": "Masked",
                "canvas": "Noise",
                "clientRect": "Noise",
                "fonts": "Masked",
                "geolocation": "Custom",
                "geolocationPopup": "Prompt",
                "gpu": "Allow",
                "localization": "Custom",
                "screen": "Custom",
                "speech": "Masked",
                "timezone": "Custom",
                "webgl": "Noise",
                "webrtc": "Custom",
            },
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.45 Safari/537.36",
            "deviceMemory": 8,
            "hardwareConcurrency": 16,
            "disableImageLoading": True,
            "doNotTrack": True,
            "localization": {
                "language": "zh-HK",
                "languages": ["zh-HK", "en-US", "en"],
                "timezone": "Asia/Hong_Kong",
            },
            "screen": {"width": 1280, "height": 1024},
            "geolocation": {
                "latitude": "31.2333",
                "longitude": "121.469",
                "accuracy": "603",
            },
            "webrtc": {"publicIp": "111.111.111.111"},
        },
        "startupUrls": ["https://www.nstbrowser.io"],
        "args": {
            "--remote-debugging-port": 34543,
            "disable-backgrounding-occluded-windows": True,
        },
    }

    try:
        # Initialize the client
        client = NstbrowserClient(api_key=api_key)
        print("Initialized NstbrowserClient, connecting to once-off browser")
        
        # Connect to the browser
        response = client.cdp_endpoints.connect_once_browser(config=config)
        print("Successfully connected to once-off browser")

        # Extract WebSocket endpoint if available
        if (
            response
            and "data" in response
            and "webSocketDebuggerUrl" in response["data"]
        ):
            ws_endpoint = response["data"]["webSocketDebuggerUrl"]
            print(f"WebSocket endpoint: {ws_endpoint}")
            return ws_endpoint
        else:
            print("WebSocket endpoint not found in response")
            if response and "data" in response:
                print(f"Available data keys: {list(response['data'].keys())}")
            return None

    except Exception as e:
        print(f"Failed to connect to once-off browser: {e}")
        return None


async def control_browser_with_playwright(websocket_url):
    try:
        # Import here to make it optional - user may not have playwright installed
        from playwright.async_api import async_playwright

        print("\nConnecting to browser with Playwright...")
        async with async_playwright() as p:
            # Connect Playwright to the existing browser via CDP
            browser = await p.chromium.connect_over_cdp(websocket_url)

            # Get the default context
            default_context = browser.contexts[0]

            # Get existing pages or create a new one if none exist
            pages = default_context.pages
            page = pages[0] if pages else await default_context.new_page()

            print("Navigating to example.com...")
            await page.goto("https://example.com")

            title = await page.title()
            print(f"Page title: {title}")

            print("Taking screenshot...")
            await page.screenshot(path="example_screenshot.png")
            print(f"Screenshot saved to example_screenshot.png")

            content = await page.text_content("h1")
            print(f"H1 content: {content}")

            print("Waiting for 3 seconds...")
            await asyncio.sleep(3)

            # Close the connection
            await page.close()
            await browser.close()
            print("Playwright connection closed")

    except ImportError:
        print(
            "Playwright is not installed. Please install it with: pip install playwright"
        )
        print("Then initialize the browsers: playwright install chromium")
    except Exception as e:
        print(f"Error during Playwright automation: {e}")


def main():
    # Step 1: Get the CDP WebSocket URL - all NstbrowserClient operations handled inside this function
    websocket_url = get_cdp_websocket_url()

    # Step 2: Use the WebSocket URL with Playwright if available
    if websocket_url:
        print("\nStarting Playwright automation...")
        asyncio.run(control_browser_with_playwright(websocket_url))
    else:
        print("Cannot proceed with Playwright automation: WebSocket URL not available")


if __name__ == "__main__":
    main()
