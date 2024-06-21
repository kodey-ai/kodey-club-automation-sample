import requests
import os

def get_daxko_token():
    url = "https://api.partners.daxko.com/auth/token"
    payload = {
        "client_id": os.getenv("DAXKO_CLIENT_ID"),
        "client_secret": os.getenv("DAXKO_CLIENT_SECRET"),
        "scope": os.getenv("DAXKO_SCOPE"),
        "grant_type": "client_credentials"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception("Failed to authenticate with Daxko API")

# Example usage
# token = get_daxko_token()
# print(token)
