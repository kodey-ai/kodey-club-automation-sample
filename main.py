import os
from member_packages import get_member_packages
from member_profile import get_member_profile

def main():
    user_id = os.getenv("USER_ID")
    try:
        print("Fetching member packages...")
        packages = get_member_packages(user_id)
        print(f"Member Packages: {packages}")

        print("Fetching member profile...")
        profile = get_member_profile(user_id)
        print(f"Member Profile: {profile}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
