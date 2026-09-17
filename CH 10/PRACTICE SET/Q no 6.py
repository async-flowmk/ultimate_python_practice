class Calculator:
    @staticmethod 
    def hello():
        print("Hey genius...")
    # Sqaure 
    def sqaure(self,num):
        self.sq = num*num
        return self.sq
        
    # Cube
    def cube(self,num):
        self.cube_val = num*(self.sqaure(num))
        return self.cube_val

    # Sqaure root
    def sqaure_root(self,num):
        self.root = num**0.5
        return self.root

n1 = Calculator()
n1.hello()
print(n1.sqaure(4),
n1.cube(4),
n1.sqaure_root(81))
