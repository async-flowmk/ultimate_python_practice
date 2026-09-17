class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,num):
        
        result = Vector(self.x + num.x,self.y + num.y,self.z + num.z)
        return result
    
    def __str__(self):
        return f"Vector ({self.x}i + {self.y}j + {self.z}k)"

    def __len__(self):
         return 3
        

v1 = Vector(2,5,7)
v2 = Vector(4,8,1)
v3 = Vector(9,6,5)

print(v1)
print(len(v1))


        