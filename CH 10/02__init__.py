# Use __init__():

class Car:
    # Default constructor
    def __init__(self):
        print("Car Showroom collection:")
    # Parameterized constructor
    def __init__(self,brand,color,model):
        self.name = brand
        self.color = color
        self.model = model
        
car1 = Car("BMW","Black","M5 cs")
print(f"This {car1.color} color {car1.name} {car1.model} is awsome!\n")

car2 = Car("Porche","Olive green","911")
print(f"This {car2.color} color {car2.name} {car2.model} is awsome!")