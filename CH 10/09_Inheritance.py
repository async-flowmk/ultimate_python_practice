# Single Inheritance:
class Car :  # Base class(Parent)
     @staticmethod
     def start():
          print("Car started...")
     @staticmethod
     def stop():
          print("Car stopped...")
class Hyundai(Car): # Derived class(child)
     def __init__(self,name):
          self.name = name
car1  = Hyundai("Sonata")
car1.start()
print(car1.name)
car1.stop()

# Multi-level inheritance:
class School: # Base class (Grand parent class)
     @staticmethod
     def school_name():
          print("School: City School")

     def __init__(self, location):
          self.location = location


class School_Branch(School): # Derived class (Child <=> parents)
     def __init__(self, location, Headmaster, no_of_std):
          super().__init__(location)
          self.principle = Headmaster
          self.No_of_students = no_of_std


class Student(School_Branch): # Child class
     def __init__(self, location, Headmaster, no_of_std, name, f_name, adm_no, Class, sec):
          super().__init__(location, Headmaster, no_of_std)

          self.name = name
          self.fatherName = f_name
          self.admission_no = adm_no
          self.Class = Class
          self.section = sec

     def info(self):
          School.school_name()
          print(f"Branch: {self.location}")
          print(f"Headmaster: {self.principle}")
          print(f"Number of Students: {self.No_of_students}")
          print(f"Student: {self.name}")
          print(f"Father's Name: {self.fatherName}")
          print(f"Class: {self.Class}")
          print(f"Section: {self.section}")
          print(f"Admission No: {self.admission_no}")


stu1 = Student(
     "DHA",
     "Prof. Iqbal",
     950,
     "Ayra",
     "Abid Dar",
     112098,
     10,
     "A"
)

stu1.info()
     
# Multiple inheritance:
class Parent_1:
     varA = "Base 1.."

class Parent_2:
     varB = "Base 2.."
     
class Child(Parent_1,Parent_2):
     varC = f"This class (Child) derivered from {Parent_1.varA} and {Parent_2.varB}"

ch1 = Child()
print(ch1.varC)
          


