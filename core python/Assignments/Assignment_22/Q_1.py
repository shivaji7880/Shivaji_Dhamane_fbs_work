class Emp:

    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def __str__(self):
        return f"{self.eid},{self.ename},{self.basic}"


FILE = "employee.txt"


# Add a record
def add_record():
    eid = input("Enter Employee ID: ")
    ename = input("Enter Employee Name: ")
    basic = input("Enter Basic Salary: ")

    with open(FILE, "a") as f:
        emp = Emp(eid, ename, basic)
        f.write(str(emp) + "\n")

    print("Record added successfully.")


# Search a record
def search_record():
    eid = input("Enter Employee ID to search: ")

    found = False

    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[0] == eid:
                print("Employee ID   :", data[0])
                print("Employee Name :", data[1])
                print("Basic Salary  :", data[2])
                found = True
                break

    if not found:
        print("Record not found.")


# Delete a record
def delete_record():
    eid = input("Enter Employee ID to delete: ")

    found = False
    records = []

    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[0] == eid:
                found = True
            else:
                records.append(line)

    with open(FILE, "w") as f:
        f.writelines(records)

    if found:
        print("Record deleted successfully.")
    else:
        print("Record not found.")


# Edit a record
def edit_record():
    eid = input("Enter Employee ID to edit: ")

    found = False
    records = []

    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[0] == eid:
                ename = input("Enter new Employee Name: ")
                basic = input("Enter new Basic Salary: ")

                emp = Emp(eid, ename, basic)
                records.append(str(emp) + "\n")

                found = True
            else:
                records.append(line)

    with open(FILE, "w") as f:
        f.writelines(records)

    if found:
        print("Record updated successfully.")
    else:
        print("Record not found.")


# Display all records
def display_records():
    try:
        with open(FILE, "r") as f:
            records = f.readlines()

            if len(records) == 0:
                print("No records available.")
            else:
                print("\n--- All Employee Records ---")

                for line in records:
                    data = line.strip().split(",")

                    print("ID     :", data[0])
                    print("Name   :", data[1])
                    print("Basic  :", data[2])
                    print("-----------------------")

    except FileNotFoundError:
        print("No records available.")


# Menu
while True:

    print("\n===== EMPLOYEE MENU =====")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()

    elif choice == "2":
        search_record()

    elif choice == "3":
        delete_record()

    elif choice == "4":
        edit_record()

    elif choice == "5":
        display_records()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")