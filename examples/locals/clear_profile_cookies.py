"""
Example demonstrating how to clear the cookies for a specific profile.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the profile ID for which you want to clear cookies
profile_id = "your_profile_id"

# Clear cookies for the specified profile
try:
    response = client.locals.clear_profile_cookies(profile_id=profile_id)
    print(f"Cookies cleared successfully for profile {profile_id}")
    print("Response:", response)
except Exception as e:
    print(f"Failed to clear profile cookies: {e}") 
