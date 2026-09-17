# Create a class named circle 
class Circle:
    # Give Radius of circle
    def __init__(self,radius):
        self.radius = radius
    
    pi_val = 3.14159 
    
    @property
    def calc_area(self):
        # A = pi r^2
        print(f"The area of circle is {round(self.pi_val*self.radius**2)}")

    @property
    def calc_perimeter(self):
        print(f"The perameter of circle is {round(2*self.pi_val*self.radius)}")
       
    @property
    def calc_diameter(self):
        print(f"The diameter of circle is {round(2*self.radius)}")
       


c1 = Circle(24)
c1.calc_area
c1.calc_perimeter
c1.calc_diameter
print("Radius was changed...")
c1.radius = 5
c1.calc_area
c1.calc_perimeter
c1.calc_diameter