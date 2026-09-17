class Complex:
    def __init__(self, real, img):
        # Constructor → values set karta hai
        self.real = real
        self.imaginary = img

    def show_num(self):
        # Number show karta hai
        print(f"{self.real}i + {self.imaginary}j")

    # Dunder function → operator ko customize karta hai
    # Yahan "+" operator overload ho raha hai
    def __add__(self, num):
        print("Add complex numbers...")

        # Dono numbers ke real parts add
        new_real = self.real + num.real

        # Dono numbers ke imaginary parts add
        new_img = self.imaginary + num.imaginary

        # New Complex object return
        return Complex(new_real, new_img)

    # "-" operator overload
    def __sub__(self, num):
        print("sub complex numbers...")

        # Real parts subtract
        new_real = self.real - num.real

        # Imaginary parts subtract
        new_img = self.imaginary - num.imaginary

        return Complex(new_real, new_img)

    # "*" operator overload
    def __mul__(self, num):
        print("mul complex numbers...")

        # Real parts multiply
        new_real = self.real * num.real

        # Imaginary parts multiply
        new_img = self.imaginary * num.imaginary

        return Complex(new_real, new_img)

    # "/" operator overload
    def __truediv__(self, num):
        print("div complex numbers...")

        # Real parts divide
        new_real = self.real / num.real

        # Imaginary parts divide
        new_img = self.imaginary / num.imaginary

        return Complex(new_real, new_img)


# Objects → Complex numbers
num1 = Complex(2, 7)
num1.show_num()

num2 = Complex(4, -2)
num2.show_num()


# "+" use kiya → Python __add__() call karega
add_complex = num1 + num2
add_complex.show_num()

# "-" use kiya → Python __sub__() call karega
sub_complex = num1 - num2
sub_complex.show_num()

# "*" use kiya → Python __mul__() call karega
mul_complex = num1 * num2
mul_complex.show_num()

# "/" use kiya → Python __truediv__() call karega
div_complex = num1 / num2
div_complex.show_num()