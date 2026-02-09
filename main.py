import json
import time
import random as rd
import tkinter as tk

x = open("./pets.json", encoding="utf8")
pets = json.load(x)
names = {}

class pet:
    all = []
    def __init__(self, name, spicies, health, hunger, happiness):
        self.name = name
        self.spicies = spicies
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        pet.all.append(self)


def createPet(pet, name):
    for p in pet.all:
        if p.name == name:
            return False
    names[name] = pet(name, pet["spicies"], pet["health"], pet["hunger"], pet["happieness"])
    return names[name]

def getRandom():
    return rd.choice(pets)

async def changeStats():
    while True:
        while len(pet.all):
            time.sleep(60)
            chHnr = rd.randrange(0,2,1)
            chHpn = rd.randrange(0,2,1)
            for p in pet.all:
                p.hunger = p.hunger - chHnr
                p.happiness = p.happiness - chHpn

def clear():
    for widget in root.winfo_children():
        widget.destroy()

def start1():
    l.destroy()
    b.destroy()
    v = tk.Label(root, text = "Your pet is...")
    v.grid(row=0, column=0)
    root.after(4000)
    p = tk.Label(root, text= "{x}!!!".format(x = (rd.choice(pets))["spicies"]))
    p.grid(row=1, column=0)
    root.after(3000)
    c = tk.Button(root, text="Continue", command=start2)
    c.grid(row=3,column=0)

def start2():
    clear()

def main():
    changeStats()
    


root = tk.Tk()


l = tk.Label(root, text = "PetSim")
l.grid(row=0, column=0)
b = tk.Button(root, text="Start", command=start1)
b.grid(row=1,column=0)
root.mainloop()