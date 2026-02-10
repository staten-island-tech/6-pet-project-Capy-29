import json
import time
import random as rd
import tkinter as tk

x = open("./pets.json", encoding="utf8")
pets = json.load(x)
names = {}

class pet:
    def __init__(self, name, spicies, health, hunger, happiness):
        self.name = name
        self.spicies = spicies
        self.health = health
        self.hunger = hunger
        self.happiness = happiness


def createPet(tPet, name):
    names[name] = pet(name, tPet["spicies"], tPet["health"], tPet["hunger"], tPet["happieness"])
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

def gr(wid, row, col):
    wid.grid(row = row, column = col)

def start1():
    l.destroy()
    b.destroy()
    v = tk.Label(root, text = "Your pet is...")
    v.grid(row=0, column=0)
    thePet = rd.choice(pets)
    p = tk.Label(root, text= "{x}!!!".format(x = thePet["spicies"].capitalize()))
    p.grid(row=1, column=0)
    c = tk.Button(root, text="Continue", command=start2)
    c.grid(row=3,column=0)

def start2():
    clear()
    l = tk.Label(root, text = "Name them!")
    gr(l, 0, 0)
    entry = tk.Entry(root)
    gr(entry, 1,0)
    bt = tk.Button(root, text = "Name", command = main)
    gr(bt, 2,0)

def main():
    createPet()
    changeStats()
    


root = tk.Tk()


l = tk.Label(root, text = "PetSim")
l.grid(row=0, column=0)
b = tk.Button(root, text="Start", command=start1)
b.grid(row=1,column=0)
root.mainloop()