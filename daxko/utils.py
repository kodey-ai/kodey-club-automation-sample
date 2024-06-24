import requests

def get_daxko_oauth_token(client_id, client_secret, scope):
    """
    Authenticate to the Daxko API and retrieve an OAuth token.
    
    :param client_id: Client ID provided by Daxko.
    :param client_secret: Client Secret provided by Daxko.
    :param scope: The ID for the customer/client you are trying to access.
    :return: OAuth token if authentication is successful, None otherwise.
    """
    url = "https://api.partners.daxko.com/auth/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope,
        "grant_type": "client_credentials"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(f"Failed to authenticate: {response.json()}")
        return None