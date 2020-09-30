# Panic! At the Dis Code

import random
import math


class Fighter:
    def __init__(self,name,strength,armor,magic):
        self.name = name
        self.health = 100
        self.strength = 50
        self.armor = 20
        self.magic = 50
        self.charge = 0
        
    def attack(self,other_fighter):
        if other_fighter.health > 0:
            damage = int((self.strength-other_fighter.armor)*random.random ())
            other_fighter.health -= damage
            print(
                f"{bcolors.RED} {self.name} attacked {other_fighter.name} for {damage} \n")
            self.charge += math.ceil(1/(damage+10) * self.magic)
            print(f"{bcolors.YELLOW} Charge: {self.charge}{bcolors.ENDC}")
            
            if other_fighter.health <= 0:
                other_fighter.health = 0
                print(
                    f"{bcolors.HEADER} Congratulations {self.name}! {other_fighter.name} lost! You are the champion!{bcolors.ENDC}\n")

    def fighter_stats(self):
        print(f"{bcolors.HEADER}Name:{self.name}{bcolors.ENDC}\n{bcolors.TGREEN}Health:{self.health}{bcolors.ENDC}\n {bcolors.CYAN} Strength: {self.strength} {bcolors.ENDC}\n {bcolors.PURPLE} Armor: {self.armor}{bcolors.ENDC}\n")
        
    def heal(self):
        amt_healed = int(self.magic * random.random())
        self.health += amt_healed
        print(f"{bcolors.PURPLE} {self.name} healed themself for {amt_healed}{bcolors.ENDC}")
        
    def special(self,other_fighter):
        if other_fighter.health > 0:
            damage = int(1.5*(self.strength-other_fighter.armor)*random.random ())
            other_fighter.health -= damage
            charge = 0
            print(
                f"\n{bcolors.RED} {self.name} SPECIAL ATTACKED {other_fighter.name} for {damage} {bcolors.ENDC} \n")
            if other_fighter.health <= 0:
                other_fighter.health = 0
                print(
                    f"{bcolors.HEADER} Congratulations {self.name}! {other_fighter.name} lost! You are the champion!{bcolors.ENDC}\n")


def fight(fighter1,fighter2):
    while(fighter1.health > 0 and fighter2.health > 0):
        print(f"{bcolors.CYAN} Name: {bcolors.ENDC}{bcolors.PURPLE}{fighter1.name}{bcolors.ENDC}, {bcolors.TGREEN} Health: {fighter1.health} {bcolors.ENDC}\n{bcolors.CYAN} Name: {bcolors.ENDC} {bcolors.PURPLE}{fighter2.name}{bcolors.ENDC}, {bcolors.TGREEN} Health: {fighter2.health} {bcolors.ENDC}\n")
        if fighter1.charge > 4:
            fighter1.special(fighter2)
        elif fighter1.health < 25:
            fighter1.heal()
        else:
            fighter1.attack(fighter2)
        if fighter2.health >0:
            if fighter2.charge > 4:
                fighter2.special(fighter1)

            elif fighter2.health <25:
                fighter2.heal()
            
            else:
                fighter2.attack(fighter1)
        

class Alien(Fighter):
    def __init__(self):
        self.name = "ET"
        self.health = 80
        self.strength = 30
        self.armor = 20
        self.magic = 40
        self.charge = 0

    def attack(self,other_fighter):
        super().attack(other_fighter)
        
    def fighter_stats(self):
        super().fighter_stats()
        

class Robot(Fighter):
    def __init__(self):
        self.name = "Adrien"
        self.health = 100
        self.strength = 50
        self.armor = 10
        self.magic = 25
        self.charge = 0
        
    def attack(self,other_fighter):
        super().attack(other_fighter)
        
    def fighter_stats(self):
        super().fighter_stats()


class Cowboy(Fighter):
    def __init__(self):
        self.name = "Farrison Hord"
        self.health = 100
        self.strength = 60
        self.armor = 20
        self.magic = 5
        self.charge = 0
        
    def attack(self,other_fighter):
        super().attack(other_fighter)
        
    def fighter_stats(self):
        super().fighter_stats()


class bcolors:
    HEADER = '\033[95m'
    TGREEN = '\033[32m'
    OKBLUE = '\029[94m'
    OKGREEN = '\021[92m'
    WARNING = '\033[93m'
    TWHITE = '\033[37m'
    FAIL = '\033[91m'
    CYAN = '\033[36m'
    PURPLE = '\033[35m'
    ENDC = '\033[0m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
