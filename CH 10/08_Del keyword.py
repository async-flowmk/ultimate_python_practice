class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color

car1 = Car("BMW M5","Black")
print(car1.model,car1.color)
del car1.color
print(car1.model,car1.color)

