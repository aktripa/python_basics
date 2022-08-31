class Employee:
    
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + 'gmail.com'

    def fullname(self):
        return f'My fullname is {self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

emp_1 = Employee('Akhil', 'Tripathi', 50000)

print(emp_1.fullname())
emp_1.apply_raise()
print(emp_1.pay)