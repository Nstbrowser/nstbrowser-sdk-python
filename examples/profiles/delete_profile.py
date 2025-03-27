"""
Example demonstrating how to delete a specific profile.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the profile ID to delete
profile_id = "461d0bf2-9de8-4e24-8bd9-c7cbf045e4aa"

# Delete the specified profile
try:
    response = client.profiles.delete_profile(profile_id=profile_id)
    print(f"Profile {profile_id} deleted successfully")
    print("Response:", response)
except Exception as e:
    print(f"Failed to delete profile: {e}") 
