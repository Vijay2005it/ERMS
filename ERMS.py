# Employee Record Management System (ERMS)

ERMS_file = 'ERMS.txt'

class erms:
    def __init__(self):
        print("Employee Record Management System (ERMS)")
        print(" 1. Add Employee")
        print(" 2. Display Employees")
        print(" 3. Search Employee")
        print(" 4. Update Employee")
        print(" 5. Delete Employee")
        print(" 6. Exit")

vijay = erms()

# ---------------- Add Employee ----------------
def add_emp():
    with open(ERMS_file, "a") as f:
        emp_id = input("Enter Employee ID : ")
        emp_name = input("Enter Employee Name : ")
        emp_age = input("Enter Employee Age : ")
        emp_dept = input("Enter Employee Department : ")
        emp_salary = input("Enter Employee Salary : ")
        f.write(f"{emp_id},{emp_name},{emp_age},{emp_dept},{emp_salary}\n")
        print("✅ Employee Added Successfully")

# ---------------- Display Employees ----------------
def display_emp():
    with open(ERMS_file, "r") as f:
        print("\n======= Employee Records =======")
        for i in f:
            print(i.strip())

# ---------------- Search Employee ----------------
def search_emp():
    emp_id_search = input("Enter Employee ID to search : ")
    found = False
    with open(ERMS_file, "r") as f:
        for i in f:
            eid, name, age, dept, salary = i.strip().split(",")
            if eid == emp_id_search:
                print(f"\n✅ Employee Found\n ID: {eid}, Name: {name}, Age: {age}, Department: {dept}, Salary: {salary}\n")
                found = True
                break
    if not found:
        print("❌ Employee Not Found")

# ---------------- Update Employee ----------------
def update_emp():
    emp_id_update = input("Enter Employee ID to Update : ")
    updated = False

    with open(ERMS_file, "r") as f:
        lines = f.readlines()
    
    with open(ERMS_file, "w") as f:
        for i in lines:
            eid, name, age, dept, salary = i.strip().split(",")
            if emp_id_update == eid:
                print(f"\n✅ Employee Found\n ID: {eid}, Name: {name}, Age: {age}, Department: {dept}, Salary: {salary}\n")
                new_id = input("Enter New ID: ")
                new_name = input("Enter New Name: ")
                new_age = input("Enter New Age: ")
                new_dept = input("Enter New Department: ")
                new_salary = input("Enter New Salary: ")
                f.write(f"{new_id},{new_name},{new_age},{new_dept},{new_salary}\n")
                print("✅ Employee Details Updated Successfully")
                updated = True
            else:
                f.write(i)
    if not updated:
        print("❌ Employee Not Found")

# ---------------- Delete Employee ----------------
def delete_emp():
    emp_id_delete = input("Enter Employee ID to Delete : ")
    deleted = False

    with open(ERMS_file, "r") as f:
        lines = f.readlines()

    with open(ERMS_file, "w") as f:
        for i in lines:
            eid, name, age, dept, salary = i.strip().split(",")
            if emp_id_delete == eid:
                print(f"\n🗑️ Employee Deleted: ID {eid}, Name {name}")
                deleted = True
                continue
            else:
                f.write(i)

    if not deleted:
        print("❌ Employee Not Found")

# ---------------- Main Menu ----------------
while True:
    user_choice = int(input("\nEnter Your Choice : "))
    if user_choice == 1:
        add_emp()
    elif user_choice == 2:
        display_emp()
    elif user_choice == 3:
        search_emp()
    elif user_choice == 4:
        update_emp()
    elif user_choice == 5:
        delete_emp()
    elif user_choice == 6:
        print("😊 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid Choice. Try again.🤦")

