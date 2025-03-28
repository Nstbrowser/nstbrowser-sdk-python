"""
Example demonstrating how to clear all tags for a specific profile.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the profile ID for which you want to clear tags
profile_id = "your_profile_id"

# Clear all tags for the specified profile
try:
    response = client.profiles.clear_profile_tags(profile_id=profile_id)
    print(f"Tags cleared successfully for profile {profile_id}")
    print("Response:", response)
except Exception as e:
    print(f"Failed to clear profile tags: {e}") 
