class Vehicle:
    def general_use(self):
        print("Used for transportation")

class Car(Vehicle):
    def __init__(self):
        print("In a car")
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self):
        print("For travelling to work")

class Bike(Vehicle):
    def __init__(self):
        print("In a bike")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self):
        print("For road trip")

hyundai = Car()
hyundai.general_use()
hyundai.specific_usage()
hyundai.wheels

honda = Bike()
honda.general_use()
honda.specific_usage()
honda.wheels

print(isinstance(honda,Bike))
print(issubclass(Bike,Vehicle))
