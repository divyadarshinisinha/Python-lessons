from abc import ABC, abstractmethod
from typing import override

class Animal(ABC):
    @abstractmethod 
    # This methsd has to be implemented in its subclass
    # compulsory
    def move(self):
        pass

    # normal method not abstract
    def test(self):
        x = 5
        y = 10
        z = x + y
        print(z)

class Snake(Animal):
    @override
    def move(self):
        print("Snakes Crawl")

class Horse(Animal):
    @override
    def move(self):
        print("Horse Kicks Back")

class Bird(Animal):
    @override
    def move(self):
        print("Birs Fly")

# S = Snake()
# S.move()

# H = Horse()
# H.move()

# B = Bird()
# B.move()


# --- Object Creation in a For Loop ---
# 1. Put the classes themselves into a list
animal_classes = [Snake, Horse, Bird]

# 2. Loop through the classes, instantiate them, and call move()
for animal_class in animal_classes:
    animal_object = animal_class()  
    # Creates the object (e.g., Snake(), Horse())
    animal_object.move()
