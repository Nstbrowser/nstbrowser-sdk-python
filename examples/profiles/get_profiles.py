"""
Example demonstrating how to get a list of profiles with optional filtering.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Get all profiles
try:
    response = client.profiles.get_profiles()
    print("All profiles:")
    print("Response:", response)
    
    # Get profiles with filtering
    filter_data = {
        "page": 1,
        "pageSize": 10,
        "s": "test",
        "tags": "",
        "groupId": ""
    }
    filtered_response = client.profiles.get_profiles(data=filter_data)
    print("\nFiltered profiles:")
    print("Response:", filtered_response)
    
except Exception as e:
    print(f"Failed to get profiles: {e}") 
