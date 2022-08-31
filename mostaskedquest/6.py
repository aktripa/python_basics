from abc import ABC,abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print(' I am a laptop')


obj1 = Computer()

obj1.process()