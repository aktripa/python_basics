class School:
    school = 'Generic'

    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName  = lastName
    
    def fullname(self):
        return f'my fullname is {self.firstName} {self.lastName}'


class Teacher(School):
    def __init__(self, firstName, lastName,subjects=[],grade=[]):
        super().__init__(firstName, lastName)
        self.subjects = grade
        self.grade = grade

    def grade(self):
        return f'i teach {self.grade}'    


