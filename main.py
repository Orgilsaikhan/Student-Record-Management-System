import os
import sys
from loading import loading_bar
from authentication import password_verification

def main():
    os.system('color 9F')  # Windows only
    # loading_bar()  # Uncomment if needed
    password_verification()

if __name__ == "__main__":
    main()