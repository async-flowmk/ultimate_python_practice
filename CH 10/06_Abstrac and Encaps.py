# Abstraction: Hidding how class works , only show the feature.
class Car:
    def __init__(self):
        self.engine = "Stop"
        self.gear = "Neutral"
    def start(self):
        self.engine = "Start"
        self.gear = "1st gear"
        print(f"Car started... Engine {self.engine} car on {self.gear}")

car1 = Car()
car1.start()

# Encapsulation : To wrap data and function in capsule (object)
class Employee:
    @staticmethod
    def hire():
        print(f"You are hired...")
    def __init__(self):
        self.qaulificaton = "MBA"
        self.experiance = 5
    def salary(self):
        if self.qaulificaton == "MBA" and self.experiance > 3:
            self.amount = "2lac"
        else:
            self.amount = "90 thousand"
        return f"{self.hire()} , your salary is {self.amount}"

emp1 = Employee()
emp1.salary()


