class student :
    collage = "ABC collage" # Class attr
    def __init__(self,name,collage):
        self.name = name
        self.collage = collage # obj attr

s1 = student("Imsaal","Bharia collage")
print(s1.name,s1.collage)

s2 = student("Ayra","City")
print(s2.name,s2.collage)
        