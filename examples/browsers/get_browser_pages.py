"""
Example demonstrating how to get pages information for a specific browser.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the profile ID for which you want to get browser pages
profile_id = "your_profile_id"

# Get pages information for the browser associated with the specified profile
try:
    response = client.browsers.get_browser_pages(profile_id=profile_id)
    print(f"Pages for browser with profile {profile_id}:")
    print("Response:", response)
    
    # Print a list of page URLs if available
    if response and "data" in response:
        pages = response["data"]
        print("\nPage info:")
        for i, page in enumerate(pages, 1):
            print(f"{i}. {page}")
except Exception as e:
    print(f"Failed to get browser pages: {e}") 
