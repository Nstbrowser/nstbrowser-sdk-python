"""
Example demonstrating how to stop multiple browsers in batch.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define a list of profile IDs for which you want to stop browsers
profile_ids = ["profile_id_1", "profile_id_2", "profile_id_3"]

# Stop browsers for the specified profiles in batch
try:
    response = client.browsers.stop_browsers(profile_ids=profile_ids)
    print(f"Browsers stopped successfully for {len(profile_ids)} profiles")
    print("Response:", response)
except Exception as e:
    print(f"Failed to stop browsers: {e}") 
