import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('adoption_page')


def get_user_data():
    """
    Get User data here
    """
    while True:
        print("Introduction to adoption page \n")
        print("1. Show available animals")
        print("2. Past/Adopted pets")
        print("3. Update")

        user_data = input('Please enter a number from 1-3 here')
        print(f"you said {user_data}")

        if user_data == '1':
            print("you said 1")
        elif user_data == '2':
            print("you said 2")
        elif user_data == '3':
            print("you said 3")
        else:
            print("you picked an invalid value \n")

get_user_data()