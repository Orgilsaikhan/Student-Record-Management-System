import os
import sys
from time import sleep
from menu import main_menu, admin_function

def password_verification():
    os.system('cls')
    while True:
        print("\n\n\n\n\n\t\t\t\t\t")
        password = input("\n\n\n\t\t\t\t\tEnter Password: ").strip()
        
        if password.lower() in ['quit', 'exit']:
            quit_program()
            
        if password == "password":
            main_menu()
            break
            
        os.system('cls')
        print("\n\n\n\n\n\t\tWrong password! Try again or type 'quit'/'exit'")

def admin_verification():
    os.system('cls')
    while True:
        password = input("\n\n\n\t\t\t\t\tEnter Admin Password: ").strip()
        
        if password.lower() == 'menu':
            main_menu()
            return
            
        if password == "password":
            admin_function()
            return
            
        os.system('cls')
        print("\n\n\n\n\n\t\tWrong password! Try 'menu' to return")

def quit_program():
    os.system('cls')
    print("\t\t\n\n\n\n\n\n\n\t\t\t\t\tQuitting The Program", end='')
    for _ in range(4):
        sleep(1)
        print(".", end='', flush=True)
    sys.exit()