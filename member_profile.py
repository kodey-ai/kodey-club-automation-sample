import requests
from utils import get_daxko_token

def get_member_profile(user_id):
    token = get_daxko_token()
    url = f"https://api.partners.daxko.com/api/v1/users/{user_id}/profile"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch member profile for user {user_id}")

# Example usage
# user_id = '410914'
# profile = get_member_profile(user_id)
# print(profile)
