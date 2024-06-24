import os
from daxko.utils import get_daxko_oauth_token
from daxko.member_packages import get_member_packages
from daxko.member_profile import get_member_profile

# Assuming the environment variables are CLIENT_ID, CLIENT_SECRET, and SCOPE
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
scope = os.getenv('SCOPE')

# Example function calls
# These functions should ideally be called within an actual application logic flow
token = get_daxko_oauth_token(client_id, client_secret, scope)
if token:
    print("Successfully authenticated.")
    # Example user ID, replace with actual user ID as needed
    user_id = 'example_user_id'
    packages = get_member_packages(client_id, client_secret, scope, user_id)
    profile = get_member_profile(client_id, client_secret, scope, user_id)
    print(f"Member Packages: {packages}")
    print(f"Member Profile: {profile}")
else:
    print("Authentication failed.")