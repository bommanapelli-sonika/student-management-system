import json
import os

FILE = "students.json"

# Load data
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save data
def save_data():
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

students = load_data()

# ADD STUDENT
def add_student():
    print("\n--- ADD STUDENT ---")
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    marks = input("Enter Marks: ")

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

    save_data()
    print("✔ Student Added Successfully!")

# VIEW STUDENTS
def view_students():
    print("\n--- STUDENT LIST ---")

    if len(students) == 0:
        print("No records found!")
        return

    for s in students:
        print("\nName :", s["name"])
        print("Roll :", s["roll"])
        print("Marks:", s["marks"])

# SEARCH STUDENT
def search_student():
    roll = input("Enter Roll No: ")

    for s in students:
        if s["roll"] == roll:
            print("\n✔ Student Found")
            print(s)
            return

    print("❌ Not Found")

# UPDATE STUDENT
def update_student():
    roll = input("Enter Roll No: ")

    for s in students:
        if s["roll"] == roll:

            new_name = input("New Name (Enter to skip): ")
            new_marks = input("New Marks (Enter to skip): ")

            if new_name:
                s["name"] = new_name

            if new_marks:
                s["marks"] = new_marks

            save_data()
            print("✔ Updated Successfully!")
            return

    print("❌ Not Found")

# DELETE STUDENT
def delete_student():
    roll = input("Enter Roll No: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_data()
            print("✔ Deleted Successfully!")
            return

    print("❌ Not Found")

# MENU
while True:
    print("\n==============================")
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you 👍")
        break
    else:
        print("Invalid choice!")