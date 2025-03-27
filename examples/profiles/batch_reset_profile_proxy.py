"""
Example demonstrating how to reset proxies for multiple profiles in batch.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define a list of profile IDs for which you want to reset proxies
profile_ids = ["profile_id_1", "profile_id_2", "profile_id_3"]

# Reset proxies for the specified profiles in batch
try:
    response = client.profiles.batch_reset_profile_proxy(profile_ids=profile_ids)
    print(f"Proxies reset successfully for {len(profile_ids)} profiles")
    print("Response:", response)
except Exception as e:
    print(f"Failed to batch reset profile proxies: {e}") 
