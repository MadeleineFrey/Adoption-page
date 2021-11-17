import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("adoption_page")


def show_available_table():
    """
    Display details of all available animals in the available worksheet,
    sheet as a table, input field to exit.
    """
    print("\033c")
    print("All available animals are listed below. \n")

    available = SHEET.worksheet("available").get_all_values()
    table = PrettyTable()
    table.field_names = ["NAME", "AGE", "SPECIES", "STATUS"]
    table.add_rows(available)
    print(table)

    main_menu_available = input("\n Press enter to return to main page \n")


def show_past_table():
    """
    Display details of all past animals in the past worksheet,
    sheet as a table, input field to exit.
    """
    print("\033c")
    print("All past animals are listed below. \n")
    past = SHEET.worksheet("past").get_all_values()
    table = PrettyTable()
    table.field_names = ["NAME", "AGE", "SPECIES", "STATUS"]
    table.add_rows(past)
    print(table)

    main_menu_past = input("\n Press enter to return to main page \n ")


def update_database():
    """
    Display the different options for the user.
    Enter a valid input value and the function will return the correct output.
    """
    while True:
        print("\033c")
        print("Welcome to the update page!")
        print("Here you can add an animal to the available list or,")
        print("update a specific animal by typing in a number between 1-4. \n")
        print("1. Show available animals")
        print("2. Add Animal")
        print("3. Update Animal")
        print("4. Back to main page \n")

        user_choice = input('\n please enter a number from 1-4 here: \n')

        if user_choice == "1":
            show_available_table()
        elif user_choice == "2":
            add_animal()
        elif user_choice == "3":
            update_available_sheet()
        elif user_choice == "4":
            get_user_data()
        else:
            print("invalid answer")


def add_animal():
    """
    Display an inputfield that takes values,
    If the value is valid execute code below in if statement.
    Run a while loop to collect a valid string of data from the user.
    The string must contain 4 values separated by commas.
    This loop will repeatedly request data, until it is valid.
    """
    print("\033c")

    while True:
        print("Please enter data about animal as shown below.")
        print("Data should be 4 values, separated by commas.\n")
        print("Name,Age,Spesiec,Status")
        print("Example: Sam,3,dog,available\n")
        print("To exit type 'x' then enter in the input field")
        add_animal_input = input("\n Enter your data here: \n")
        add_animal_data = add_animal_input.split(",")

        if add_animal_input == "x":
            update_database()
        else:
            if validate_add_data(add_animal_data):
                available_worksheet = SHEET.worksheet("available")
                available_worksheet.append_row(add_animal_data)
                break

    return add_animal_data


def validate_add_data(values):
    """
    Takes one parameter and return true/false depending on the parameter.
    Inside the try, Raises ValueError if there aren't exactly 6 values.
    """
    print("\033c")
    try:
        if len(values) != 4:
            raise ValueError(
                f"you need exactly 4 values, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"invalid data: {e}, try again")
        return False

    return True


def update_available_sheet():
    """
    Display the different options for the user.
    Enter a valid input value and the function will return the correct output.
    """
    while True:
        print("\033c")
        print("Welcome! Here you can watch available and past animals,")
        print("Update a specific animal by entering a number between 1-4.\n")
        print("1. Show available animals")
        print("2. Past/Adopted pets")
        print("3. Delete available animal")
        print("4. Back to main page/Exit \n")

        update_choice = input("\n please enter a number from 1-4 here: \n")

        if update_choice == "1":
            show_available_table()
        elif update_choice == "2":
            show_past_table()
        elif update_choice == "3":
            delete_row()
        elif update_choice == "4":
            get_user_data()
        else:
            print("invalid answer")


def delete_row():
    """
    Display inputfield that takes values and if the value is valid:
    execute code below in if statement.
    Run a while loop to collect a valid string of data from the user.
    The string must contain a value.
    This loop will repeatedly request data, until it is valid.

    When there is a valid input value execute the code inside the if statement.
    """
    print("\033c")

    while True:
        print("To delete an animal enter the row-number of that one animal")
        print("Exemple:")
        print("To delet an animal in the first row type in the number '1'.\n")
        print("To exit type 'x' then enter in the input field.")
        delete_input = input("Enter your data here: \n")

        if delete_input == "x":
            update_available_sheet()
        else:
            if validate_delete_data(delete_input):
                delete = int(delete_input)
                SHEET.worksheet("available").delete_rows(delete)
                break

    return delete_input


def validate_delete_data(valuess):
    """
    Takes one parameter and return true/false depending on the parameter.
    Inside the try,
    Raises ValueError if there aren't a value and,
    If it's not posible to converts the string value into a integer.
    """
    print("\033c")
    try:
        [int(value) for value in valuess]
        if len(valuess) < 1:
            raise ValueError(
                f"you need exactly 4 values, you provided {valuess}"
            )
    except ValueError as e:
        print(f"invalid data: {e}, try again")
        return False

    return True


def get_user_data():
    """
    Get input from the user.
    Run a while loop to collect a valid string of data from the user
    """
    while True:
        print("\033c")
        print("Welcome to the Adoption page!") 
        print("Here, you can look at all of the available animals,")
        print("as well as the animals we have had before. \n")
        print("You can also add an animal to the available sheet or,")
        print("update a specific animal.\n")
        print("1. Show available animals")
        print("2. Past/Adopted pets")
        print("3. Update")

        user_data = input("\n Please enter a number from 1-3 here: \n")

        if user_data == "1":
            show_available_table()
        elif user_data == "2":
            show_past_table()
        elif user_data == "3":
            update_database()
        else:
            print(f"You picked an invalid value")

get_user_data()
