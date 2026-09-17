class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        super().__init__("Data scientist","IT","2lac")

    def show_info(self):
        print(f"Employee name is {self.name}")
        print(f"Employee age is {self.age}")
        print(f"Employee role is {self.role}")
        print(f"Employee Department is {self.department}")
        print(f"Employee Salary is {self.salary}")

       

emp1 = Engineer("Mustafa","18 years")
emp1.show_info()
        