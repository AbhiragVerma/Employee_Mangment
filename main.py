from employee import (
    FullTimeEmployee,
    PartTimeEmployee,
    Manager
)

from company import Company

company = Company()

while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Remove Employee")
    print("5. Calculate Total Payroll")
    print("6. Payroll Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\n1. Full Time Employee")
        print("2. Part Time Employee")
        print("3. Manager")

        employee_type = input(
            "Select Employee Type: "
        )

        employee_id = input("Employee ID: ")
        name = input("Name: ")
        department = input("Department: ")

        if employee_type == "1":

            monthly_salary = float(
                input("Monthly Salary: ")
            )

            employee = FullTimeEmployee(
                employee_id,
                name,
                department,
                monthly_salary
            )
        elif employee_type == "2":

                    hourly_rate = float(
                        input("Hourly Rate: ")
                    )

                    hours_worked = float(
                        input("Hours Worked: ")
                    )

                    employee = PartTimeEmployee(
                        employee_id,
                        name,
                        department,
                        hourly_rate,
                        hours_worked
                    )
    
        elif employee_type == "3":

            monthly_salary = float(
                input("Monthly Salary: ")
            )

            bonus = float(
                input("Bonus: ")
            )

            employee = Manager(
                employee_id,
                name,
                department,
                monthly_salary,
                bonus
            )

    if choice == "2":
        company.display_all_employees()

    elif choice == "3":

        employee_id = input("Enter Employee ID: ")

        employee = company.find_employee(employee_id)

        if employee:
            print(employee.display_details())
        else:
            print("Employee not found.")

    elif choice == "4":

        employee_id = input("Enter Employee ID: ")

        if company.remove_employee(employee_id):
            print("Employee removed successfully.")
        else:
            print("Employee not found.")

    elif choice == "5":

        print(
            "Total Payroll:",
            company.calculate_total_payroll()
        )

    elif choice == "6":
        company.generate_payroll_report()

    elif choice == "7":
        print("Exiting...")
        break

    if company.add_employee(employee):
        print("Employee added successfully.")
    else:
        print("Employee ID already exists.")
