class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + 'email.com'

    def fullname(self):
        return f'{self.first} {self.last}'    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang       

class Manager(Employee):

    def __init__(self, first, last, pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        pass
                
    

dev_2 = Developer('Saschin','Tendulkar',800000,'Java')
dev_1 = Developer('Akhil','Tripathi',500000,'Python')

print(dev_1.email)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.email)