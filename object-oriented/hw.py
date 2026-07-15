class ProductBlueprint:
    # Constructor
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Method to display product details
    def displayDetails(self):
        return f"Product: {self.name}\nCategory: {self.category}\nPrice: ₹{self.price}"

    # Method to calculate discounted price
    def calculateDiscount(self, discount_percentage):
        discount = (self.price * discount_percentage) / 100
        new_price = self.price - discount
        return new_price


# Creating two product objects
product1 = ProductBlueprint("Laptop", 50000, "Electronics")
product2 = ProductBlueprint("Shoes", 3000, "Footwear")

# Displaying details
print(product1.displayDetails())
print("Price after 10% discount: ₹", product1.calculateDiscount(10))

print()

print(product2.displayDetails())
print("Price after 20% discount: ₹", product2.calculateDiscount(20))