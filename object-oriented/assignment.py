class CarBluePrint: 
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def displayDetails(self):
        return f"The car's brand is {self.brand}, model is {self.model}, and the year is {self.year}"

car1 = CarBluePrint("Toyota", "Fortuner", 2023)
car2 = CarBluePrint("Honda", "City", 2022)

print(car1.displayDetails())
print(car2.displayDetails())