class Students: # => Class

    collage = "ABC" # => Class attributes

    def __init__(self,# => Self parameter 
                 name,
                 rollNo,
                 marks,
                 faculty
                 ): # => __init__() constructor

    # => Objects attributes
        self.name = name 
        self.marks = marks
        self.roll_no = rollNo
        self.faculty = faculty

    def get_info(self): # => Method 
        return f"""{self.name} get {self.marks} marks.\nThe Roll no is {self.roll_no} and choose {self.faculty} in {self.collage} collage"""
    
    def greet(self):# Method(function)
        print(f"Welcome student\n{self.get_info()}")

s1 = Students("Ayra",12,94,"Computer science") # => Object
s1.greet()



        