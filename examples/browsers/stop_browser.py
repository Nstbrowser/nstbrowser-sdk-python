"""
Example demonstrating how to stop a browser for a specific profile.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the profile ID for which you want to stop the browser
profile_id = "your_profile_id"

# Stop the browser for the specified profile
try:
    response = client.browsers.stop_browser(profile_id=profile_id)
    print(f"Browser stopped successfully for profile {profile_id}")
    print("Response:", response)
except Exception as e:
    print(f"Failed to stop browser: {e}") 
