class Human:
    #initialises the properties of the class when we later try to create an instance
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "chef":
            print(self.name, "is a", self.occupation)
        elif self.occupation == "barber":
            print(self.name,"is a",self.occupation)
        else:
            print(self.name, "isn't a chef or barber")

    def speaks(self):
        print(self.name, ": How do you do?")

laila = Human("Laila","barber")
laila.do_work()
laila.speaks()

majnu = Human("Majnu", "actor")
majnu.do_work()
majnu.speaks()
