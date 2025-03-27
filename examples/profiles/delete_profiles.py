"""
Example demonstrating how to delete multiple profiles in batch.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define a list of profile IDs to delete
profile_ids = ["profile_id_1", "profile_id_2", "profile_id_3"]

# Delete multiple profiles in batch
try:
    response = client.profiles.delete_profiles(profile_ids=profile_ids)
    print(f"Successfully deleted {len(profile_ids)} profiles")
    print("Response:", response)
except Exception as e:
    print(f"Failed to delete profiles: {e}") 
