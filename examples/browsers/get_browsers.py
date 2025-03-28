"""
Example demonstrating how to get a list of browsers with optional status filtering.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Get all browsers
try:
    response = client.browsers.get_browsers()
    print("All browsers:")
    print("Response:", response)
    
    # Get browsers with a specific status (e.g., starting,running,stopping)
    status_response = client.browsers.get_browsers(status="running")
    print("\nRunning browsers:")
    print("Response:", status_response)
except Exception as e:
    print(f"Failed to get browsers: {e}") 
