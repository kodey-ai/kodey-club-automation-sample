import requests
from .utils import get_daxko_oauth_token

def get_member_profile(client_id, client_secret, scope, user_id):
    """
    Retrieves a member's profile from Daxko API.
    
    :param client_id: Client ID for Daxko API.
    :param client_secret: Client Secret for Daxko API.
    :param scope: Scope ID for the customer/client.
    :param user_id: User ID of the member whose profile is to be retrieved.
    :return: JSON response containing member profile if successful, None otherwise.
    """
    token = get_daxko_oauth_token(client_id, client_secret, scope)
    if token:
        url = f"https://api.partners.daxko.com/api/v1/users/{user_id}/profile"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve member profile: {response.json()}")
            return None
    else:
        print("Failed to authenticate.")
        return None