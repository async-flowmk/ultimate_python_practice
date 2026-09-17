class Animals:
    def __init__(self,type_animal):
        self.type = type_animal
class Pets(Animals):
    def __init__(self, type_animal,):
        super().__init__(type_animal)
        if type_animal == "Pet animal":
            print("It is a pet animal")
        else:
            pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow...bow..")

an1 = Dog("Pet animal")
an1.bark()
        