class Company:

    def __init__(self):
        self._employees = {}
    
    def add_employee(self, employee):

        if employee.employee_id in self._employees:
            return False

        self._employees[employee.employee_id] = employee
        return True
    
    def find_employee(self, employee_id):
        return self._employees.get(employee_id)