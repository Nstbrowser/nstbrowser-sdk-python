"""
Example demonstrating how to create tags for a specific profile.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the profile ID and tags data
profile_id = "your_profile_id"
data = [
    {"name": "social", "color": "#646AEE"},
    {"name": "marketing", "color": "#646AEE"},
    {"name": "testing", "color": "#646AEE"},
]


# Create tags for the specified profile
try:
    response = client.profiles.create_profile_tags(
        profile_id=profile_id, data=data
    )
    print(f"Tags created successfully for profile {profile_id}: {data}")
    print("Response:", response)
except Exception as e:
    print(f"Failed to create profile tags: {e}")
