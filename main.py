import json
x = open("./pets.json", encoding="utf8")
pets = json.load(x)

class pet:
    all = []
    def __init__(self, name, spicies, health, hunger, happiness):
        self.name = name
        self.spicies = spicies
        self.health = health
        self.hunger = hunger
        self.happiness = happiness


def createPet(pet, name):
    "{x}".format(x = name) = pet(name, pet["spicies"], pet["health"], pet["happieness"])

def save():
    pets = json.load(x)
    for pet in pets:
        pet.pop()
    open("./pets.json", "w").write(
        
    )
