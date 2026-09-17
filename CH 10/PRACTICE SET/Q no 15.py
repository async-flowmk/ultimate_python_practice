class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,num):
        
        result = Vector(self.x + num.x,self.y + num.y,self.z + num.z)
        return result
    
    def __mul__(self,num):
        
        result = Vector(self.x * num.x,self.y * num.y,self.z * num.z)
        return result
    def __str__(self):
        return f"Vector ({self.x}, {self.y}, {self.z})"

v1 = Vector(2,5,7)
v2 = Vector(4,8,1)
v3 = Vector(9,6,5)

print(v1 + v2)
print(v1 + v2 + v3)
print(v1 + v2 * v3)
print(v1 * v2)
        