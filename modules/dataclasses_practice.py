from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Employee(ABC):
    name: str
    position: str
    age: int
    experience: int
    salary: float
    date_joined: field(default_factory=datetime)

    def get_max_salary(self):
        return self.salary * self.experience / (self.age + self.experience)


class SalariedEmployee(Employee):

    def print_type(self):
        return 'This is a salaried employee'


salaried_employee = SalariedEmployee(
    name='Kevin', position='Lead', age=25, experience=3, salary=1000, date_joined=datetime.today())

print(salaried_employee.print_type())
