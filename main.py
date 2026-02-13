import json
import time
import random as rd
import tkinter as tk
import asyncio

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
    names[name] = pet(name, tPet["spicies"], tPet["health"], tPet["hunger"], tPet["happiness"])
    return names[name]

def getRandom():
    return rd.choice(pets)

async def updateStats():
    while True:
        print("ran")
        time.sleep(10)
        chHnr = rd.randrange(0,2,1)
        chHpn = rd.randrange(0,2,1)
        names[petName].hunger = names[petName].hunger - chHnr
        names[petName].happiness = names[petName].happiness - chHpn
        if names[petName].hunger < 0:
            names[petName].hunger = 0
            names[petName].health = names[petName].health - chHnr
        if names[petName].happiness < 0:
            names[petName].happiness = 0
            names[petName].health = names[petName].health - chHpn
    
def doPet():
    chHpn = rd.randrange(0,2,1)
    names[petName].happiness = names[petName].happiness + chHpn
    if names[petName].happiness > 10:
        names[petName].happiness = 10
    happiness.config(text = "happiness: {}".format(names[petName].happiness))
    root.update()

def doFeed():
    chHnr = rd.randrange(0,2,1)
    names[petName].hunger = names[petName].hunger + chHnr
    if names[petName].hunger > 10:
        names[petName].hunger = 10
    hunger.config(text = "hunger: {}".format(names[petName].hunger))
    root.update()

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
    root.update()
    time.sleep(2)
    global thePet
    thePet = rd.choice(pets)
    p = tk.Label(root, text= "{x}!!!".format(x = thePet["spicies"].capitalize()))
    p.grid(row=1, column=0)
    root.update()
    time.sleep(1)
    c = tk.Button(root, text="Continue", command=start2)
    c.grid(row=3,column=0)

def start2():
    clear()
    l = tk.Label(root, text = "Name them!")
    gr(l, 0, 0)
    global en
    en = tk.Entry(root)
    gr(en, 1,0)
    bt = tk.Button(root, text = "Name", command = main)
    gr(bt, 2,0)


def main():
    global petName
    global name
    global spicies
    global health
    global hunger
    global happiness
    petName = en.get()
    clear()
    
    createPet(thePet, petName)
    name = tk.Label(root, text="Name: {}".format(names[petName].name))
    gr(name, 0,0)
    spicies = tk.Label(root, text = "Spicies: {}".format(names[petName].spicies))
    gr(spicies, 1,0)
    health = tk.Label(root, text = "Health: {}".format(names[petName].health))
    gr(health, 2,0)
    hunger = tk.Label(root, text = "Hunger: {}".format(names[petName].hunger))
    gr(hunger,3,0)
    happiness = tk.Label(root, text = "Happiness: {}".format(names[petName].happiness))
    gr(happiness,4,0)
    petBt = tk.Button(root, text = "Pet", command = doPet)
    gr(petBt, 5,0)
    feedBt = tk.Button(root, text = "Feed", command = doFeed)
    gr(feedBt, 6,0)
    root.update()
    asyncio.run(updateStats())
    while True:
        time.sleep(0.2)
        name.config(text="name: {}".format(names[petName].name))
        spicies.config(text = "spicies: {}".format(names[petName].spicies))
        health.config(text = "health: {}".format(names[petName].health))
        hunger.config(text = "hunger: {}".format(names[petName].hunger))
        happiness.config(text = "happiness: {}".format(names[petName].happiness))
        root.update()
        print("1")

root = tk.Tk()


l = tk.Label(root, text = "PetSim")
l.grid(row=0, column=0)
b = tk.Button(root, text="Start", command=start1)
b.grid(row=1,column=0)
root.mainloop()