"""
Example demonstrating how to clear tags for multiple profiles in batch.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define a list of profile IDs for which you want to clear tags
profile_ids = ["profile_id_1", "profile_id_2", "profile_id_3"]

# Clear tags for multiple profiles in batch
try:
    response = client.profiles.batch_clear_profile_tags(profile_ids=profile_ids)
    print(f"Tags cleared successfully for {len(profile_ids)} profiles")
    print("Response:", response)
except Exception as e:
    print(f"Failed to batch clear profile tags: {e}") 
