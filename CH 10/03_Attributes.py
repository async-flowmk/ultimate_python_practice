class Car:
    # Parameterized constructor
    brand = "Honda" # class attr
    name = "Any" # class attr
    def __init__(self,color,name):
        self.name = name # obj attr > class attr
        self.color = color
        
        
car1 = Car("White","Civic")
print(f"This {car1.color} color {car1.brand} {car1.name} is awsome!")

 