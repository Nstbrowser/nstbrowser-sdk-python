"""
Example demonstrating how to change groups for multiple profiles in batch.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define batch data for changing profile groups
batch_data = {
    "profileIds": ["profile_id_1", "profile_id_2", "profile_id_3"],
    "groupId": "target_group_id"
}

# Change groups for multiple profiles in batch
try:
    response = client.profiles.batch_change_profile_group(data=batch_data)
    print(f"Groups changed successfully for {len(batch_data['profileIds'])} profiles")
    print("Response:", response)
except Exception as e:
    print(f"Failed to change profile groups in batch: {e}")