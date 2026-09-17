class Student:
    def __init__(self,phy,math,eng):
        self.physic = phy
        self.maths = math
        self.english = eng
    @property # Convert method in property (attributes),you use as instance attri:
    def calc_percentage(self):
        total_marks = 300
        sum_subj = self.physic + self.maths + self.english
        percent = round(sum_subj/total_marks * 100)
        return str(percent) + "%"

stu1 = Student(96,87,91)
print(stu1.calc_percentage)

print("After Re-checking...")
stu1.maths = 76
print("Maths marks was actually is:",stu1.maths)
print(stu1.calc_percentage)