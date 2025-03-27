"""
Example demonstrating how to start a once-off browser with custom configuration.
"""

import os
from nstbrowser import NstbrowserClient

# Initialize the client with your API key
api_key = os.environ.get("NSTBROWSER_API_KEY", "your_api_key")
client = NstbrowserClient(api_key=api_key)

# Define the configuration for the once-off browser
config = {
    "name": "testProfile",
    "platform": "Windows",
    "kernelMilestone": "132",
    "autoClose": True,
    "timedCloseSec": 30,
    "headless": False,
    "incognito": False,
    "proxy": "http://admin:123456@127.0.0.1:8000",
    "skipProxyChecking": True,
    "fingerprint": {
        "flags": {
            "audio": "Noise",
            "battery": "Masked",
            "canvas": "Noise",
            "clientRect": "Noise",
            "fonts": "Masked",
            "geolocation": "Custom",
            "geolocationPopup": "Prompt",
            "gpu": "Allow",
            "localization": "Custom",
            "screen": "Custom",
            "speech": "Masked",
            "timezone": "Custom",
            "webgl": "Noise",
            "webrtc": "Custom",
        },
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.45 Safari/537.36",
        "deviceMemory": 8,
        "hardwareConcurrency": 16,
        "disableImageLoading": True,
        "doNotTrack": True,
        "localization": {
            "language": "zh-HK",
            "languages": ["zh-HK", "en-US", "en"],
            "timezone": "Asia/Hong_Kong",
        },
        "screen": {"width": 1280, "height": 1024},
        "geolocation": {
            "latitude": "31.2333",
            "longitude": "121.469",
            "accuracy": "603",
        },
        "webrtc": {"publicIp": "111.111.111.111"},
    },
    "startupUrls": ["https://www.nstbrowser.io"],
    "args": {
        "--remote-debugging-port": 34543,
        "disable-backgrounding-occluded-windows": True,
    },
}

# Start a once-off browser with the specified configuration
try:
    response = client.browsers.start_once_browser(data=config)
    print("Once-off browser started successfully")
    print("Response:", response)
except Exception as e:
    print(f"Failed to start once-off browser: {e}")
