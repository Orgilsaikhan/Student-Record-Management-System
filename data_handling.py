import csv
import os
import tempfile
from menu import admin_function
CSV_FILE = "students.csv"

def add_data():
    os.system('cls')
    print("\t|Enter Data|")
    
    fields = [
        "Roll Number", "Name", "College", "Branch",
        "Attendance", "Physics", "Chemistry", "Maths"
    ]
    
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        data = [input(f"\nEnter Student's {field}: ") for field in fields]
        writer.writerow(data)
    
    if input("\nAdd more Record? (Y/N): ").lower() == 'y':
        add_data()
    else:
        admin_function()

def delete_data():
    os.system('cls')
    rollnum = input("Enter roll number to delete: ")
    
    rows = []
    found = False
    
    with open(CSV_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != rollnum:
                rows.append(row)
            else:
                found = True
    
    if found:
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Record deleted")
    else:
        print("Record not found")
    
    input("\nPress Enter to continue...")
    admin_function()

def view_data():
    os.system('cls')
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            print("\n\t\t\t\t\t\t|Students Record| \n")
            print("Roll\tName\t\tCollege\t\tBranch\t\tAttendance\tPhysics\t\tChemistry\tMaths")
            for row in reader:
                if row:
                    print("\t".join(row))
    except FileNotFoundError:
        print("No records found")
    
    input("\nPress Enter to continue...")