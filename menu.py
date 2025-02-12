import os
# With this:
def add_data(): from data_handling import add_data; return add_data()
def delete_data(): from data_handling import delete_data; return delete_data()
def view_data(): from data_handling import view_data; return view_data()
from authentication import admin_verification, quit_program
# Move this to the TOP of the file
def student_function():
    from data_handling import view_data
    os.system('cls')
    print("Welcome Student")
    view_data()
    input("\nPress Enter to return to main menu...")
    main_menu()

# Then keep the existing main_menu() and admin_function()
def main_menu():
    os.system('cls')
    print("\n\n\n\n\t\t\t\t\t Login As : ")
    print("\n\n\n\t\t\t\t\t 1. Admin ")
    print("\n\n\t\t\t\t\t 2. Student")
    print("\n\n\t\t\t\t\t 3. Exit")
    
    choice = input("\n\n\n\t\t\t\t\t Enter your choice: ")
    
    if choice == '1':
        admin_verification()
    elif choice == '2':
        student_function()
    elif choice == '3':
        quit_program()
    else:
        print("Invalid input!")
        main_menu()

def admin_function():
    os.system('cls')
    print("\n\n\t\t\t\t\t | Logged In as Admin |\n")
    print("\n\n\t\t\t\t\t 1. Add Students Detail")
    print("\n\n\t\t\t\t\t 2. Delete Students")
    print("\n\n\t\t\t\t\t 3. View Table ")
    print("\n\n\t\t\t\t\t 4. Main Menu ")
    print("\n\n\t\t\t\t\t 5. Exit")
    
    choice = input("\n\n\t\t\t\t\tEnter choice: ")
    
    if choice == '1':
        add_data()
    elif choice == '2':
        delete_data()
    elif choice == '3':
        view_data()
    elif choice == '4':
        main_menu()