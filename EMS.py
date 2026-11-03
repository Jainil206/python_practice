
employees = [
    {"id": 101, "name": "Jainil", "age": 25, "department": "IT",
     "designation": "Python Developer", "salary": 40000,
     "performance": "Good", "bonus": 0, "tax_deduction": 0,
     "attendance": 30, "leave": 0},

    {"id": 102, "name": "Dhruv", "age": 28, "department": "HR",
     "designation": "HR Manager", "salary": 50000,
     "performance": "Excellent", "bonus": 0, "tax_deduction": 0,
     "attendance": 30, "leave": 0},

    {"id": 103, "name": "Nil", "age": 32, "department": "Finance",
     "designation": "Accountant", "salary": 35000,
     "performance": "Average", "bonus": 0, "tax_deduction": 0,
     "attendance": 30, "leave": 0}
]


def find_employee(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None


def add_employee():
    employee_id = int(input("Enter Employee ID: "))

    if find_employee(employee_id):
        print("Employee ID already exists!")
        return

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Monthly Salary: "))

    if name == "" or age <= 0 or department == "" or designation == "" or salary <= 0:
        print("Enter valid employee details!")
        return

    employee = {
        "id": employee_id,
        "name": name,
        "age": age,
        "department": department,
        "designation": designation,
        "salary": salary,
        "performance": "Average",
        "bonus": 0,
        "tax_deduction": 0,
        "attendance": 30,
        "leave": 0
    }

    employees.append(employee)
    print("Employee added successfully!")


def display_employees():
    if len(employees) == 0:
        print("No employees available!")
        return

    print("\n------------- EMPLOYEE RECORDS -------------")
    print("ID\tName\t\tDepartment\tSalary")

    for employee in employees:
        print(
            employee["id"], "\t",
            employee["name"], "\t\t",
            employee["department"], "\t\t",
            employee["salary"]
        )


def search_employee():
    employee_id = int(input("Enter Employee ID to search: "))

    employee = find_employee(employee_id)

    if employee:
        print("\nEmployee Found!")
        print("ID:", employee["id"])
        print("Name:", employee["name"])
        print("Age:", employee["age"])
        print("Department:", employee["department"])
        print("Designation:", employee["designation"])
        print("Monthly Salary:", employee["salary"])
        print("Performance:", employee["performance"])
        print("Bonus:", employee["bonus"])
        print("Tax Deduction:", employee["tax_deduction"])
        print("Attendance:", employee["attendance"])
        print("Leave:", employee["leave"])
    else:
        print("Employee not found!")


def update_employee():
    employee_id = int(input("Enter Employee ID to update: "))
    employee = find_employee(employee_id)

    if not employee:
        print("Employee not found!")
        return

    print("1. Update Name")
    print("2. Update Age")
    print("3. Update Department")
    print("4. Update Designation")
    print("5. Update Salary")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter new name: ")
        if name != "":
            employee["name"] = name
            print("Name updated successfully!")
        else:
            print("Invalid name!")

    elif choice == "2":
        age = int(input("Enter new age: "))
        if age > 0:
            employee["age"] = age
            print("Age updated successfully!")
        else:
            print("Invalid age!")

    elif choice == "3":
        department = input("Enter new department: ")
        if department != "":
            employee["department"] = department
            print("Department updated successfully!")
        else:
            print("Invalid department!")

    elif choice == "4":
        designation = input("Enter new designation: ")
        if designation != "":
            employee["designation"] = designation
            print("Designation updated successfully!")
        else:
            print("Invalid designation!")

    elif choice == "5":
        salary = float(input("Enter new monthly salary: "))
        if salary > 0:
            employee["salary"] = salary
            print("Salary updated successfully!")
        else:
            print("Invalid salary!")

    else:
        print("Invalid choice!")


def delete_employee():
    employee_id = int(input("Enter Employee ID to delete: "))
    employee = find_employee(employee_id)

    if employee:
        employees.remove(employee)
        print("Employee deleted successfully!")
    else:
        print("Employee not found!")


# NEW FEATURE 1: Performance-based bonus

def calculate_bonus():
    employee_id = int(input("Enter Employee ID: "))
    employee = find_employee(employee_id)

    if not employee:
        print("Employee not found!")
        return

    print("\n1. Excellent - 20% Bonus")
    print("2. Good - 10% Bonus")
    print("3. Average - 5% Bonus")
    print("4. Poor - No Bonus")

    choice = input("Enter your choice: ")

    if choice == "1":
        percentage = 20
        employee["performance"] = "Excellent"
    elif choice == "2":
        percentage = 10
        employee["performance"] = "Good"
    elif choice == "3":
        percentage = 5
        employee["performance"] = "Average"
    elif choice == "4":
        percentage = 0
        employee["performance"] = "Poor"
    else:
        print("Invalid choice!")
        return

    employee["bonus"] = employee["salary"] * percentage / 100

    print("Performance:", employee["performance"])
    print("Bonus Percentage:", percentage, "%")
    print("Bonus Amount:", employee["bonus"])
    print("Bonus calculated successfully!")


# NEW FEATURE 2: Tax-saving deduction

def update_tax_deduction():
    employee_id = int(input("Enter Employee ID: "))
    employee = find_employee(employee_id)

    if not employee:
        print("Employee not found!")
        return

    deduction = float(input("Enter eligible annual tax-saving deduction: "))

    if deduction < 0:
        print("Invalid deduction amount!")
        return

    employee["tax_deduction"] = deduction
    print("Tax deduction updated successfully!")


# NEW FEATURE 3: Salary slip and tax calculation

def generate_salary_slip():
    employee_id = int(input("Enter Employee ID: "))
    employee = find_employee(employee_id)

    if not employee:
        print("Employee not found!")
        return

    monthly_salary = employee["salary"]
    monthly_bonus = employee["bonus"]

    annual_income = (monthly_salary + monthly_bonus) * 12

    annual_deduction = min(
        employee["tax_deduction"], annual_income
    )

    taxable_income = annual_income - annual_deduction

    # Educational flat-rate tax estimate (10%)
    annual_tax = taxable_income * 10 / 100
    monthly_tax = annual_tax / 12

    gross_salary = monthly_salary + monthly_bonus
    net_salary = gross_salary - monthly_tax

    print("\n========== EMPLOYEE SALARY SLIP ==========")
    print("Employee ID:", employee["id"])
    print("Employee Name:", employee["name"])
    print("Department:", employee["department"])
    print("------------------------------------------")
    print("Basic Salary:", monthly_salary)
    print("Performance Bonus:", monthly_bonus)
    print("Gross Salary:", gross_salary)
    print("------------------------------------------")
    print("Annual Income:", annual_income)
    print("Eligible Annual Deduction:", annual_deduction)
    print("Estimated Taxable Income:", taxable_income)
    print("Estimated Monthly Tax:", round(monthly_tax, 2))
    print("------------------------------------------")
    print("NET MONTHLY SALARY:", round(net_salary, 2))
    print("==========================================")


# NEW FEATURE 4: Attendance and leave management

def update_attendance():
    employee_id = int(input("Enter Employee ID: "))
    employee = find_employee(employee_id)

    if not employee:
        print("Employee not found!")
        return

    print("1. Update Present Days")
    print("2. Update Leave Days")

    choice = input("Enter your choice: ")

    if choice == "1":
        days = int(input("Enter present days (0-31): "))

        if 0 <= days <= 31:
            employee["attendance"] = days
            print("Attendance updated successfully!")
        else:
            print("Invalid number of days!")

    elif choice == "2":
        days = int(input("Enter leave days (0-31): "))

        if 0 <= days <= 31:
            employee["leave"] = days
            print("Leave updated successfully!")
        else:
            print("Invalid number of days!")

    else:
        print("Invalid choice!")


# NEW FEATURE 5: Department-wise employee search

def search_department():
    department = input("Enter Department Name: ").strip().lower()

    found = False

    for employee in employees:
        if employee["department"].lower() == department:
            print("\nEmployee Found!")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Designation:", employee["designation"])
            print("Salary:", employee["salary"])
            found = True

    if not found:
        print("No employees found in this department!")


# NEW FEATURE 6: Company salary report

def company_salary_report():
    if len(employees) == 0:
        print("No employees available!")
        return

    total_salary = 0
    total_bonus = 0

    for employee in employees:
        total_salary += employee["salary"]
        total_bonus += employee["bonus"]

    print("\n========== COMPANY SALARY REPORT ==========")
    print("Total Employees:", len(employees))
    print("Total Monthly Basic Salary:", total_salary)
    print("Total Monthly Bonus:", total_bonus)
    print("Total Monthly Payroll:", total_salary + total_bonus)
    print("===========================================")


# MAIN MENU

while True:
    print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")

    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Calculate Employee Bonus")
    print("7. Update Tax-saving Deduction")
    print("8. Generate Salary Slip")
    print("9. Update Attendance and Leave")
    print("10. Search Employee by Department")
    print("11. Company Salary Report")
    print("12. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        calculate_bonus()

    elif choice == "7":
        update_tax_deduction()

    elif choice == "8":
        generate_salary_slip()

    elif choice == "9":
        update_attendance()

    elif choice == "10":
        search_department()

    elif choice == "11":
        company_salary_report()

    elif choice == "12":
        print("Thank you for using Employee Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
