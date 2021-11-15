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

def update_database():
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
            available_table()
        elif user_choice == '2':
            print('You picked 2')
            add_animal()

        elif user_choice == '3':
            print('You picked 3')
            

        elif user_choice == '4':
            print('you picked 4')
            get_user_data()
        else:
            print("invalid answer")
            #input('please enter a number from 1-4 here: ')
    
def add_animal():
    """
    t
    """
    print("\033c")

    while True:
        print('How the user is suposed to write their answer, separated by commas \n')
        
        add_animal_input = input('\n Enter your data here: ')
        
        add_animal_data = add_animal_input.split(",")

        if validate_add_data(add_animal_data):
            #call the update_add_animal_worksheet function instead?
            print('valid')
            available_worksheet = SHEET.worksheet('available')
            available_worksheet.append_row(add_animal_data)
            print('it is working \n')
            break

    return add_animal_data


def validate_add_data(values):
    """ 
    there need to be exactly 4 values
    """
    print("\033c")
    #print(values)
    try:
        #[int(value) for value in values]
        if len(values) != 4:
            raise ValueError(
                f'you need exactly 4 values, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'invalid data: {e}, try again')
        return False

    return True

def update_add_animal_worksheet(data):
    """
    t
    """
    #print("updating available worksheet... \n")
    #available_worksheet = SHEET.available
    #available_worksheet.append_row(data)
    #print('it is working \n')

def get_user_data():
    """
    Get User data here
    """
    
    while True:
        print("Introduction to adoption page \n")
        print("1. Show available animals")
        print("2. Past/Adopted pets")
        print("3. Update")
        print("4. if there is time, aply for adoption")

        user_data = input('\n Please enter a number from 1-3 here: ')

        if user_data == '1':
            print("you picked 1")
            available_table()
            
        elif user_data == '2':
            print("you picked 2")
            past_table()
        elif user_data == '3':
            print("you picked 3")
            update_database()
        else:
            print("you picked an invalid value \n")

        print("\033c")

    


get_user_data()

#data = add_animal()
#add_data = [int(val) for val in data]
#update_add_animal_worksheet(data)