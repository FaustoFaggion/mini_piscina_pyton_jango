class HotBeverage:
    name = "hot beverage"
    price = 0.30
    
    def __init__(self):
        pass
    
    def description(self):
        return "just some hot water in a cup."
    
    def __str__(self):
        return "name: " + str(self.name) + "\n" +  "price: " + "{:0.2f}".format(self.price) + "\n" + "description: " + str(self.description())
    

class Coffee(HotBeverage):
    
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40
        
    def description(self):
        return "A coffee, to stay awake."
        
class Tea(HotBeverage):
    
    def __init__(self):
        self.name = 'tea'
        
    def description(self):
        return "just some hot water in a cup"
    
class Chocolate(HotBeverage):
    
    def __init__(self):
        self.name = "chocolate"    
        self.price = 0.50
    def description(self):
        return "Chocolate, sweet chocolate..."
    
class Cappuccino(HotBeverage):
    
    def __init__(self):
        self.name = "cappuccino"
        self.price = 0.45
            
    def description(self):
        return "Un po' di Italia nella sua taza!"
