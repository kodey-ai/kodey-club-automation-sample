import requests
from utils import get_daxko_token

def get_member_packages(user_id):
    token = get_daxko_token()
    url = f"https://api.partners.daxko.com/api/v1/users/{user_id}/packages"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch member packages for user {user_id}")

# Example usage
# user_id = '410914'
# packages = get_member_packages(user_id)
# print(packages)


import requests
from .utils import get_daxko_oauth_token

def get_member_packages(client_id, client_secret, scope, user_id):
    """
    Retrieves member packages from Daxko API.
    
    :param client_id: Client ID for Daxko API.
    :param client_secret: Client Secret for Daxko API.
    :param scope: Scope ID for the customer/client.
    :return: JSON response containing member packages if successful, None otherwise.
    """
    token = get_daxko_oauth_token(client_id, client_secret, scope)
    if token:
        url = f"https://api.partners.daxko.com/api/v1/users/{user_id}/packages"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve member packages: {response.json()}")
            return None
    else:
        print("Failed to authenticate.")
        return None