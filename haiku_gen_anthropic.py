import requests
import os

# Load the API key from environment variables
API_KEY = os.getenv("ANTHROPIC_API_KEY")

url = "https://api.anthropic.com/v1/messages"
headers = {
    "x-api-key": API_KEY,
    "content-type": "application/json",
    "anthropic-version": "2023-06-01"
}

data = {
    "model": "claude-3-sonnet-20240229",
    "messages": [{"role": "user", "content": "Write a haiku about the ocean."}]
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.json()["content"])
else:
    print(f"Error: {response.status_code} - {response.text}")
