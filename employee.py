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
    
class PartTimeEmployee(Employee):

    def __init__(
        self,
        employee_id,
        name,
        department,
        hourly_rate,
        hours_worked_per_month
    ):
        super().__init__(employee_id, name, department)

        self._hourly_rate = hourly_rate
        self._hours_worked_per_month = hours_worked_per_month

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        self._hourly_rate = hourly_rate

    @property
    def hours_worked_per_month(self):
        return self._hours_worked_per_month

    @hours_worked_per_month.setter
    def hours_worked_per_month(self, hours_worked_per_month):
        self._hours_worked_per_month = hours_worked_per_month

    def calculate_salary(self):
        return self._hourly_rate * self._hours_worked_per_month

    def display_details(self):
        return (
            f"{super().display_details()}, "
            f"Hourly Rate: {self._hourly_rate}, "
            f"Hours Worked: {self._hours_worked_per_month}"
        )

    def to_dict(self):
        return {
            "type": "parttime",
            "employee_id": self._employee_id,
            "name": self._name,
            "department": self._department,
            "hourly_rate": self._hourly_rate,
            "hours_worked_per_month": self._hours_worked_per_month
        }