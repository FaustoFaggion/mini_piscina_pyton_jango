import random
from beverages import *

class CoffeeMachine:
    
    service = 0
    
    def __init__(self):
        pass
    
    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90
        
        def description(self):
            return "An empty cup?! Gimme my money back!"
        
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.service = 0
        return
    
    def serve(self, hot_beverage):
        flag = random.randrange(0, 2)
        if self.service == 10:
            raise self.BrokenMachineException()
        else:
            self.service = self.service + 1
            if flag == 0:
                return self.EmptyCup()
            else:
                return hot_beverage()
    
    
if __name__ == '__main__':
    a = CoffeeMachine()
    i = 0
    while(i < 12):
        try:
            s = a.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino]))
            print(s)
        except Exception as e:
            print(e)
        i += 1
    a.repair()
    while(i < 12):
        try:
            s = a.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino]))
            print(s)
        except Exception as e:
            print(e)
        i += 1