class Person:
    name = None
    # def __init__(self,name):
    #     # Person.name = name (1st way to change class attri)
    #     # self.__class__.name = name (2nd way)
    # ==========================
    # @class method (3rd way)
    # Take class as first argument...
    # Give access to change class attributes.
    # ==========================
    @classmethod
    def change_name(cls,name):
        cls.name = name

p1= Person()
p1.change_name("Maryam")
print(p1.name)
print(Person.name)