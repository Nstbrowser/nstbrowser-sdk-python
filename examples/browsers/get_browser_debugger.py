"""
Example demonstrating how to get debugger information for a specific browser.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the profile ID for which you want to get browser debugger information
profile_id = "your_profile_id"

# You need to start the profile before you can get debugger information
try:
    response = client.browsers.get_browser_debugger(profile_id=profile_id)
    print(f"Debugger information for browser with profile {profile_id}:")
    print("Response:", response)
    
    # Extract and print the debugger URL if available
    if response and "data" in response and "webSocketDebuggerUrl" in response["data"]:
        debugger_url = response["data"]["webSocketDebuggerUrl"]
        print(f"\nDebugger URL: {debugger_url}")
except Exception as e:
    print(f"Failed to get browser debugger information: {e}") 
