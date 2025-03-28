"""
Example demonstrating how to get all profile tags.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Get all profile tags
try:
    response = client.profiles.get_profile_tags()
    print("Profile tags retrieved successfully")
    print("Response:", response)
    
    # Print a list of all unique tags if available
    if response and "data" in response:
        tags = response["data"]
        print("\nAvailable tags:")
        for i, tag in enumerate(tags, 1):
            print(f"{i}. {tag}")
except Exception as e:
    print(f"Failed to get profile tags: {e}") 
