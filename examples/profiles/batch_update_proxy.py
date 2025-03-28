"""
Example demonstrating how to update proxies for multiple profiles in batch.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the proxy data for batch update
proxy_data = {
    "profileIds": ["profile_id_1", "profile_id_2", "profile_id_3"],
    "proxyConfig": {
        "url": "http://admin:654321@127.0.0.1:8000",
    },
}

# Update proxies for the specified profiles in batch
try:
    response = client.profiles.batch_update_proxy(data=proxy_data)
    print(f"Proxies updated successfully for {len(proxy_data['profileIds'])} profiles")
    print("Response:", response)
except Exception as e:
    print(f"Failed to batch update proxies: {e}")
