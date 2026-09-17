class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.img = imaginary

    def __add__(self,num):
        print("Adding...")
        newReal = self.real + num.real
        newImg = self.img + num.img
        return Complex(newReal,newImg)

    def __mul__ (self,num):
        print("Multiplying...")
        newReal = self.real * num.real
        newImg = self.img * num.img
        return Complex(newReal,newImg)

    def show(self):
        print(f"{self.real}i + {self.img}j")

num1 = Complex(12,7)
num1.show()
num2 = Complex(5,-3)
num2.show()



add = num1 + num2
add.show()

mul= num1 * num2
mul.show()
    