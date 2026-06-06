from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, employee_id, name, department):
        self._employee_id = employee_id
        self._name = name
        self._department = department

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def name(self):
        return self._name

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        return (
            f"ID: {self._employee_id}, "
            f"Name: {self._name}, "
            f"Department: {self._department}"
        )

    def to_dict(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, employee_id, name, department, monthly_salary):
        super().__init__(employee_id, name, department)
        self._monthly_salary = monthly_salary

    @property
    def monthly_salary(self):
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, monthly_salary):
        self._monthly_salary = monthly_salary

    def calculate_salary(self):
        return self._monthly_salary

    def display_details(self):
        return (
            f"{super().display_details()}, "
            f"Monthly Salary: {self._monthly_salary}"
        )

    def to_dict(self):
        return {
            "type": "fulltime",
            "employee_id": self._employee_id,
            "name": self._name,
            "department": self._department,
            "monthly_salary": self._monthly_salary
        }
    
