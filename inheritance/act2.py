# Inheritance in OOP
class GrandPa:
    def __init__(self, name, money, car):
        self.name = name
        self.car = car
        self.money = money
    
    def displayAsset(self):
        return f"{self.name} has ${self.money} and also a {self.car} car"

class GrandSon(GrandPa):
    def __init__(self, name, money, car, laptop):
        GrandPa.__init__(self, name, money, car)
        self.laptop = laptop
    
    def displayAsset(self):
        return f"{GrandPa.displayAsset(self)}, and {self.laptop} laptop"

gs1 = GrandSon("Kevin", "25,00,000", "Toyota Corolla", "Hp Pavillion")
print(gs1.displayAsset())