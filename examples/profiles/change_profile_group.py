"""
Example demonstrating how to change a profile's group.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define profile ID and target group ID
profile_id = "your_profile_id"
group_id = "target_group_id"

# Change the profile's group
try:
    response = client.profiles.change_profile_group(profile_id=profile_id, group_id=group_id)
    print(f"Profile {profile_id} moved to group {group_id} successfully")
    print("Response:", response)
except Exception as e:
    print(f"Failed to change profile group: {e}")
