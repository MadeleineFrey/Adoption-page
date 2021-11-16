import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
table = PrettyTable()
x = PrettyTable()

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
    Display details of all available animals in the available worksheet,
    sheet as a table using PrettyTables
    """
    print("\033c")
    available = SHEET.worksheet("available").get_all_values()
    table.field_names = ['NAME', 'AGE', 'SPECIE', 'STATUS']
    table.add_rows(available)

    print(table)

    main_menu_available = input("\n Press enter to return to main page")


def past_table():
    """
    Display details of all past animals in the past worksheet,
    sheet as a table using PrettyTables
    """
    print("\033c")
    past = SHEET.worksheet("past").get_all_values()
    x.field_names = ['NAME', 'AGE', 'SPECIE', 'STATUS']
    x.add_rows(past)
    print(x)

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

        user_choice = input('\n please enter a number from 1-4 here: \n')

        if user_choice == '1':
            print("works")
            available_table()
        elif user_choice == '2':
            print('You picked 2')
            add_animal()

        elif user_choice == '3':
            print('You picked 3')
            update_available_sheet()

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
        
        add_animal_input = input('\n Enter your data here: \n')
        
        add_animal_data = add_animal_input.split(",")

        if validate_add_data(add_animal_data):
            print('valid')
            available_worksheet = SHEET.worksheet('available')
            available_worksheet.append_row(add_animal_data)
            print('it is working \n')
            break

    return add_animal_data


def validate_add_data(values):
    """ 
    There need to be exactly 4 values
    """
    print("\033c")
    try:
        if len(values) != 4:
            raise ValueError(
                f'you need exactly 4 values, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'invalid data: {e}, try again')
        return False

    return True


def update_available_sheet():
    """
    t
    """
    print("\033c")
    while True:
        print("Introduction to update page \n")
        print("1. Delete available animal")
        print("2. Move available animal to past")
        print("3. Back to main page/Exit \n")

        update_choice = input('\n please enter a number from 1-4 here: \n')

        if update_choice == '1':
            print("works")
            delete_row()
        elif update_choice == '2':
            print('You picked 2')
            update_row()

        elif update_choice == '3':
            print('You picked 3')
            get_user_data()
        else:
            print("invalid answer")


def delete_row():
    """
    h
    """
    print("\033c")

    while True:
        print('How the user is suposed to write their answer, separated by commas \n')

        delete_input = input('\n Enter your data here: \n')

        if validate_delete_data(delete_input):
            print('delete')
            print(delete_input)
            r = SHEET.worksheet('available')
            w = r.row_values(delete_input)
            print(w)
            break

    return delete_input


def validate_delete_data(valuess):
    """ 
    there need to be exactly 4 values
    """
    print("\033c")
    try:
        [int(value) for value in valuess]
        if len (valuess) < 1:
            raise ValueError(
                f'you need exactly 4 values, you provided {valuess}'
            )
    except ValueError as e:
        print(f'invalid data: {e}, try again')
        return False

    return True


def update_row():
    #while True:
    #add 3 difrent inputs for row col val
        print('Ex 1, 1, "Bella" \n')

        update_row_input = input('\n Enter your data here: \n')
        av = SHEET.worksheet('available')
        av.update_cell(row, col, value)

        #if validate_update_row(update_row_input):
           
            #av = SHEET.worksheet('available')
            #av.update(update_row_input)

            #break

    #return update_row_input

def validate_update_row(valuess):
    """ 
    there need to be exactly 4 values
    """
    print("\033c")
    try:
    
        if len (valuess) < 1:
            raise ValueError(
                f'you need exactly 4 values, you provided {valuess}'
            )
    except ValueError as e:
        print(f'invalid data: {e}, try again')
        return False

    return True



def get_user_data():
    """
    Get User input data here
    """
    print("\033c")
    while True:
        print("Introduction to adoption page \n")
        print("1. Show available animals")
        print("2. Past/Adopted pets")
        print("3. Update")
        print("4. if there is time, aply for adoption")

        user_data = input('\n Please enter a number from 1-3 here: \n')

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