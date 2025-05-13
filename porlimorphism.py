# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves.")

# Subclasses with different move() implementations
class Car(Vehicle):
    def move(self):
        print("🚗 The car is being driven.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying.")

class Boat(Vehicle):
    def move(self):
        print("🛥️ The boat is sailing.")

# Demonstrating polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
