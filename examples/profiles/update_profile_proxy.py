"""
Example demonstrating how to update a proxy for a specific profile.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the profile ID for which you want to update the proxy
profile_id = "your_profile_id"
proxy_config = {
    "url": "http://admin:654321@127.0.0.1:8000",
}

# Update the proxy for the specified profile
try:
    response = client.profiles.update_profile_proxy(
        profile_id=profile_id, data=proxy_config
    )
    print(f"Proxy updated successfully for profile {profile_id}")
    print("Response:", response)
except Exception as e:
    print(f"Failed to update profile proxy: {e}")
