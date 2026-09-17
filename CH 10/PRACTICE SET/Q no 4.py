class Calculator:
    def __init__(self,num):
        self.num = num
        
    # Sqaure 
    def sqaure(self):
        return self.num*self.num
        
    # Cube
    def cube(self):
          return self.num*(self.num*self.num)
          

    # Sqaure root
    def sqaure_root(self):
        return  self.num**0.5
         

n1 = Calculator(40)

print(f"Square of {n1.num} num = {n1.sqaure()}\nCube of {n1.num} = {n1.cube()}\nSquare root of {n1.num}  = {n1.sqaure_root()}")