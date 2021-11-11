import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('adoption_page')

def available_table():
    """
    t
    """
    print("\033c")
    available = SHEET.worksheet("available").get_all_values()
    pprint(available)

    main_menu_available = input("\n Press enter to return to main page")


def past_table():
    """
    t
    """
    print("\033c")
    past = SHEET.worksheet("past").get_all_values()
    pprint(past)

    main_menu_past = input("\n Press enter to return to main page")

def update_page():
    """
    t
    """
    print("\033c")
    while True:
        print("Introduction to update page \n")
        print("1. Show available animals")
        print("2. Add Animal")
        print("3. Update Animal")
        print("4. Back to main page \n")

        user_choice = input('\n please enter a number from 1-4 here: ')

        if user_choice == '1':
            print("works")
        else:
            print("invalid answer")
            input('please enter a number from 1-4 here: ')

def get_user_data():
    """
    Get User data here
    """
    
    while True:
        print("Introduction to adoption page \n")
        print("1. Show available animals")
        print("2. Past/Adopted pets")
        print("3. Update")

        user_data = input('\n Please enter a number from 1-3 here: ')

        if user_data == '1':
            print("you picked 1")
            available_table()
            
        elif user_data == '2':
            print("you picked 2")
            past_table()
        elif user_data == '3':
            print("you picked 3")
            update_page()
        else:
            print("you picked an invalid value \n")

        print("\033c")


get_user_data()