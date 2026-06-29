# Create Class
class HouseBluePrint:
    # construction in python OOP
    def _init_(self,color,floors, rooms):
        self.color = color
        self.floors = floors
        self.rooms = rooms
    def displayDetails(self):
        return f"My House color is {self.color}, it has {self.floors} floors and {self.rooms} rooms"
    
# Create Object
# Infinite object you can make

h1 = HouseBluePrint("Brown", 2, 7)
h2 = HouseBluePrint("Blue", 3, 13)

print(h1.displayDetails())
print(h2.displayDetails())