class TwoD_vector:
    def __init__(self,first_D,sec_D):
        self.first_D = first_D
        self.sec_D = sec_D
    def show(self):
        print(f"{self.first_D}i + {self.sec_D}j")


class ThreeD_vector(TwoD_vector):
    def __init__(self, first_D, sec_D,third_D):
        super().__init__(first_D, sec_D)
        self.third_D = third_D
    def show(self):
        print(f"{self.first_D}i + {self.sec_D}j + {self.third_D}k")

n1 = ThreeD_vector(23,-5,12)
n1.show()


         