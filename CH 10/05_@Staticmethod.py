# Create class named student :
class Student:

    @staticmethod #=> Decorator
    def stu_class():
        return "2nd year"
    
    # Take name & marks of 3 sub as arguments in constructor
    def __init__(self,name,phy,math,urdu):
        self.name = name
        self.marks = [phy,math,urdu]
    # Method to print the avg
    def calc_avg(self):
        val = sum(self.marks)
        avg = round(val / 3)
        return f"{self.stu_class()} {self.name}\nAverage of 3 subjects is {avg} "

s1 = Student("Imsaal",99,78,65)
# s1.name = "Ayra"
print(s1.calc_avg())
