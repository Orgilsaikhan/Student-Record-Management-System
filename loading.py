import time
import os

def loading_bar():
    os.system('cls')
    os.system('color 9F')  # Windows only
    print("\n\t\t\t\t\tProject By Ajay Singh")
    print("\n\n\n\t\t\t\t\tLoading...\n")
    print("\t\t\t\t\t" + "□" * 26, end='\r')
    
    for _ in range(26):
        print("■", end='', flush=True)
        time.sleep(0.2)