class Father:
    def skills(self):
        print("Programmer")

class Mother:
    def skills(self):
        print("Gardening")

class Child(Father, Mother):
    def __init__(self, name):
        self.name = name
    def skills(self):
        print(self.name,"likes Sports")
        Father.skills(self)
        Mother.skills(self)

me = Child("Pai")
me.skills()

dad = Father()
dad.skills()