class Pet:

    def __init__(self, name="Spot", type="Dog", tricks="Fetch", health=100, energy=100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def petStatus(self):
        print(self.health)
        print(self.energy)

    def noise(self):
        print("bark bark bark")

spot = Pet("Spot", "dog", "fetch")