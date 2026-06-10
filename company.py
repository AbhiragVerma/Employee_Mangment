from employee import (
    FullTimeEmployee,
    PartTimeEmployee,
    Manager
)
import json

class Company:

    def __init__(self):
        self._employees = {}
        self._data_file = "employees.json"
        self._load_data()
    
    def add_employee(self, employee):

        if employee.employee_id in self._employees:
            return False

        self._employees[employee.employee_id] = employee
        self._save_data()
        return True
    
    def find_employee(self, employee_id):
        return self._employees.get(employee_id)
    
    def remove_employee(self, employee_id):

        if employee_id in self._employees:
            del self._employees[employee_id]
            self._save_data()

            return True

        return False

    def display_all_employees(self):

        for employee in self._employees.values():
            print(employee.display_details())

    def calculate_total_payroll(self):

        total = 0

        for employee in self._employees.values():
            total += employee.calculate_salary()

        return total
    
    def generate_payroll_report(self):
        print("\n===== Payroll Report =====")

        for employee in self._employees.values():
            print(
                f"ID: {employee.employee_id}, "
                f"Name: {employee.name}, "
                f"Salary: {employee.calculate_salary()}"
            )
            
        print("\nTotal Payroll:", self.calculate_total_payroll())

    def _save_data(self):

        employee_list = []

        for employee in self._employees.values():
            employee_list.append(employee.to_dict())

        with open(self._data_file, "w") as file:
            json.dump(employee_list, file, indent=4)

    def _load_data(self):

        try:

            with open(self._data_file, "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            return
        
        for employee_data in data:

            employee_type = employee_data["type"]

            if employee_type == "fulltime":

                employee = FullTimeEmployee(
                    employee_data["employee_id"],
                    employee_data["name"],
                    employee_data["department"],
                    employee_data["monthly_salary"]
                )

            elif employee_type == "parttime":

                employee = PartTimeEmployee(
                    employee_data["employee_id"],
                    employee_data["name"],
                    employee_data["department"],
                    employee_data["hourly_rate"],
                    employee_data["hours_worked_per_month"]
                )

            elif employee_type == "manager":

                employee = Manager(
                    employee_data["employee_id"],
                    employee_data["name"],
                    employee_data["department"],
                    employee_data["monthly_salary"],
                    employee_data["bonus"]
                )

            self._employees[employee.employee_id] = employee
        
   