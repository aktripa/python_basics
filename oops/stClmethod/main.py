import datetime

class Employee:
    raise_amt = 1.04
    number_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + 'email.com'

        Employee.number_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
                return False
        return True            

emp_1 = Employee('Akhil','Tripathi',500000)
emp_string_2 = 'Sachin-Tendulkar-200000'

emp_2 = Employee.from_string(emp_string_2)
print(emp_2.fullname())

my_date = datetime.date(2022,6,26)

print(Employee.is_workday(my_date))