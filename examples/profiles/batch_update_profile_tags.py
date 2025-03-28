"""
Example demonstrating how to update tags for multiple profiles in batch.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the batch update tags data
batch_update_data = {
    "profileIds": ["profile_id_1", "profile_id_2", "profile_id_3"],
    "tags": [
        {"name": "social", "color": "#646AEE"},
        {"name": "marketing", "color": "#646AEE"},
        {"name": "testing", "color": "#646AEE"},
    ],
}

# Update tags for multiple profiles in batch
try:
    response = client.profiles.batch_update_profile_tags(data=batch_update_data)
    print(
        f"Tags {batch_update_data['tags']} updated for {len(batch_update_data['profileIds'])} profiles"
    )
    print("Response:", response)
except Exception as e:
    print(f"Failed to batch update profile tags: {e}")
