"""
Example demonstrating how to connect to a browser using Chrome DevTools Protocol
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
    profile_id = "d261ff21-9c1c-4832-a003-057e92b691a7"
    config = {
        "headless": False,  # False to see the browser UI
        "autoClose": False,  # False to keep the browser open after the script ends
    }

    try:
        # Initialize the client
        client = NstbrowserClient(api_key=api_key)
        print(f"Initialized NstbrowserClient, connecting to profile: {profile_id}")

        # Connect to the browser
        response = client.cdp_endpoints.connect_browser(
            profile_id=profile_id, config=config
        )
        print(f"Successfully connected to browser for profile {profile_id}")

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
            return None

    except Exception as e:
        print(f"Failed to connect to browser: {e}")
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
