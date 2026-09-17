#=============================================
# PARENT / BASE CLASS
#=============================================
# Commerce is the main (parent) class.
# It contains information that can be common to students,
# such as their class/year.
class Commerce:
    def __init__(self, which_class):
        self._class_ = which_class
# ============================================
# CHILD CLASS OF COMMERCE
# ============================================
# Subjects inherits from Commerce.
#
# Syntax:
# class ChildClass(ParentClass):
#
# This means Subjects can use the attributes and methods
# available in Commerce.
class Subjects(Commerce):
    def __init__(self, which_class, total_sub, fav_sub):
        # super() is used to call the parent class.
        #
        # Here, super().__init__(which_class)
        # calls:
        #
        # Commerce.__init__(which_class)
        #
        # This allows Commerce to create '_class_' for us.
        super().__init__(which_class)

        # Store the total number of subjects in the object.
        #
        # Example:
        # total_sub = 7
        self.subject = total_sub

        # Store the student's favorite subject.
        #
        # Example:
        # fav_sub = "Accounting"
        self.favSubject = fav_sub
# ===========================================
# STUDENT CLASS
# ===========================================
# Student inherits from Subjects.
#
# IMPORTANT:
# Subjects already inherits from Commerce.
#
# Therefore, Student indirectly inherits from Commerce too.
#
# Inheritance chain:
#
# Student
#    ↓
# Subjects
#    ↓
# Commerce
#
# This is called MULTILEVEL INHERITANCE.
class Student(Subjects):
    def __init__(self, which_class, total_sub, fav_sub,
                 name, roll_no, collage_name):
        # Call the constructor of the parent class (Subjects).
        #
        # Subjects will receive:
        # which_class
        # total_sub
        # fav_sub
        #
        # Then Subjects will use:
        # super().__init__(which_class)
        #
        # to call Commerce.
        #
        # Complete flow:
        #
        # Student → Subjects → Commerce
        super().__init__(which_class, total_sub, fav_sub)

        # These attributes belong specifically to Student.
        self.name = name
        self.collage = collage_name
        self.Roll_No = roll_no
    # ============================================
    # METHOD
    # ============================================
    # This method displays the complete information
    # stored inside the Student object.
    def info(self):
        print(f"Student name : {self.name}")
        print(f"Collage name : {self.collage}")
        print(f"Roll no. {self.Roll_No}")
        print(f"Which year : {self._class_}")
        print(f"Total subjects : {self.subject}")
        print(f"Favorite subjects : {self.favSubject}")
# ============================================================
# CREATING AN OBJECT
# ============================================================
# Here we create an object named 'stu1' from the Student class.
#
# The values are passed in the same order as the
# Student.__init__() parameters:
#
# 1. which_class
# 2. total_sub
# 3. fav_sub
# 4. name
# 5. roll_no
# 6. collage_name
stu1 = Student(
    "2nd year",
    7,
    "Accounting",
    "Mustafa",
    11089,
    "Government Commerce and Economics collage"
)
# ============================================================
# CALLING THE METHOD
# ============================================================
stu1.info()

