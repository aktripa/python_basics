class Fruit:
    def __init__(self,name):
        self.name = name
    
    def fruitName(self):
        return f'I am {self.name} fruit'

class Citrus(Fruit):
    def __init__(self,name,type):
        super().__init__(name)
        self.type = type

    def fruitType(self):
        return (self.fruitName() + f' and I am also {self.type}') 

fruit_1 = Citrus('Lemon','Citrus')

print(fruit_1.fruitType())