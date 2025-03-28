"""
Example demonstrating how to update tags for a specific profile.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the profile ID and updated tags data
profile_id = "your_profile_id"

update_tags_data = [
    {"name": "social", "color": "#646AEE"},
    {"name": "marketing", "color": "#646AEE"},
    {"name": "testing", "color": "#646AEE"},
]

# Update tags for the specified profile
try:
    response = client.profiles.update_profile_tags(
        profile_id=profile_id, data=update_tags_data
    )
    print(
        f"Tags updated successfully for profile {profile_id}: {update_tags_data}"
    )
    print("Response:", response)
except Exception as e:
    print(f"Failed to update profile tags: {e}")
