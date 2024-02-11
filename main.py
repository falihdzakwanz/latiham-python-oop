# print("hello world")

class Hero:
    
    def __init__(self, inputName, inputAge, inputSchool):
        self.name = inputName
        self.age = inputAge
        self.scool = inputSchool


hero1 = Hero("najib", 22, "Man 1 Bandar Lampung");

print(hero1.__dict__)