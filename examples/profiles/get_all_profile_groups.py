"""
Example demonstrating how to get all profile groups.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Get all profile groups
try:
    response = client.profiles.get_all_profile_groups()
    print("All profile groups retrieved successfully")
    print("Response:", response)
    
    # Optionally, you can filter by group name
    group_name = "MyGroup"
    filtered_response = client.profiles.get_all_profile_groups(group_name=group_name)
    print(f"Profile groups filtered by name '{group_name}':", filtered_response)
except Exception as e:
    print(f"Failed to get profile groups: {e}")
