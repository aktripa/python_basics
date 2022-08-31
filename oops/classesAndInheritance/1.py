class Vehicle:
    color = 'White'

    def __init__(self,type,usage):
        self.type = type
        self.usage = usage



class Bus(Vehicle):
    color = 'Yellow'

    def __init__(self,type,usage,engine,model):
        super().__init__(type,usage)
        self.engine = engine
        self.model = model

    def vehicle_name(self):
        return f'{self.model} \n {self.type} \n {self.color} \n {self.engine} \n {self.usage}'

class MiniBus(Bus,Vehicle):
    pass

vehicle_1 = MiniBus('Commercial Vehical','School Transport','3000','TATA')

print(vehicle_1.vehicle_name())

        