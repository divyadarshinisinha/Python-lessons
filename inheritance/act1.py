# Inheritance in OOP
class GrandPa:
    def __init__(self, name, money, car):
        self.name = name
        self.car = car
        self.money = money
    
    def displayAsset(self):
        return f"{self.name} has ${self.money} and also a {self.car} car"

class GrandSon(GrandPa):
    pass

gp1 = GrandPa("Mr. John", "25,00,000", "Toyota Corolla")
print(gp1.displayAsset())