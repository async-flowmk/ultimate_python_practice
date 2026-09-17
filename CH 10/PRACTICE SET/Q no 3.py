class Programmer:
    company = "Microsoft"
    def __init__(self,name,age,qaulification,experiance):
        self.name = name
        self.qaulification = qaulification
        self.age = age 
        self.experiance = experiance
    def info(self):
        print(f"The employee name is {self.name}.\nAge {self.age}years old")
        print(f"{self.experiance} experiance.\nQaulification is {self.qaulification}\n")

emp1 = Programmer("Ali",24,"Master in CS","2 year")
emp1.info()

emp2 = Programmer("Umer",21,"MBA",None)
emp2.info()

emp3 = Programmer("Sarah",25,"Deploma in DSA","1.5 year")
emp3.info()


