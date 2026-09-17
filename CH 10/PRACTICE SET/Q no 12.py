class Employee:
    def __init__(self,salary,increment):
        self.__salary = salary 
        self.__increment = increment

    @property
    def salaryAfter_increment(self):
        salary = (self.__salary * self.__increment/100)
        return self.__salary + salary
    def show(self):
        print(f"Your previous salary was {self.__salary}\nAfter Increment {self.salaryAfter_increment}")

    


emp1 = Employee(250000,5)
emp1.show()