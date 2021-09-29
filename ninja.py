from pet import Pet

class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet()

    def walk(self):
        self.pet.play()
        self.pet.petStatus()

    def feed(self):
        self.pet.eat()
        self.pet.petStatus()

    def bathe(self):
        self.pet.noise()

bob = Ninja("Bob", "Smith", "rawhide", "kibbles")

bob.bathe()