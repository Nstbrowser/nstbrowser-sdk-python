"""
Example demonstrating how to reset a proxy for a specific profile.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the profile ID for which you want to reset the proxy
profile_id = "your_profile_id"

# Reset the proxy for the specified profile
try:
    response = client.profiles.reset_profile_proxy(profile_id=profile_id)
    print(f"Proxy reset successfully for profile {profile_id}")
    print("Response:", response)
except Exception as e:
    print(f"Failed to reset profile proxy: {e}") 
