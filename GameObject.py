# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:48:42 2023

@author: cleme
"""

from turtle import *
from Carte import *
import random as rdm
import matplotlib.pyplot as plt

class Player():
    
    def __init__(self):
        self.t = Turtle()
        self.tresors = 0
    
    def turn(self):
        return
        
class Map():
    
    def __init__(self):
        self.t = Turtle()
        self.t.hideturtle()
        self.state = {"pontAvantDroit":[0,pontAvantDroit], "pontMilieuDroit":[0,pontMilieuDroit],
                      "pontArrDroit":[0,pontArrDroit], "pontAvantGauche":[0,pontAvantGauche],
                      "pontMilieuGauche":[0,pontMilieuGauche], "pontArrGauche":[0,pontArrGauche],
                      "moteur":[0,moteur], "cabine":[0,cabine], "buffet":[0,buffet], 
                      "tapis":[0,tapis], "tables":[0,tables],"pontAvant":[0,pontAvant],
                      "pontArriere":[0,pontArriere], "chambresGauche":[0,chambresGauche],
                      "chambresDroite":[0,chambresDroite], "salleSecrete":[0,salleSecrete]}
        
        self.initMap()
        
    def initMap(self):
        pontAvantDroit(self.t)
        pontMilieuDroit(self.t)
        pontArrDroit(self.t)
        pontAvantGauche(self.t)
        pontMilieuGauche(self.t)
        pontArrGauche(self.t)
        moteur(self.t)
        cabine(self.t)
        buffet(self.t)
        tapis(self.t)
        tables(self.t)
        chambresDroite(self.t)
        chambresGauche(self.t)
        salleSecrete(self.t)
        pontAvant(self.t)
        pontArriere(self.t)
        bateauDroit(self.t)
        bateauGauche(self.t)
        
    def sinking(self, place):
        if (self.state[place][0] == 2):
            print("Le terrain est déjà innondé.")
        else:
            self.state[place][0] += 1 
            if (self.state[place][0] == 1):
                print("Le terrain est en train de sombrer.")
                self.state[place][1](self.t, sinking=True)
            elif(self.state[place[0] == 2]):
                print("Le terrain est innondé.")
                self.state[place][1](self.t, sunk=True)
        return self.state[place][0]
    
    def drying(self, place):
        if (self.state[place][0] == 0):
            print("Le terrain est déjà sec.")
        elif (self.state[place][0] == 2):
            print("Le terrain est innondé et ne peut pas être assècher.")
        else:
            print("Le terraine est asséché.")
            self.state[place][0] -= 1
            self.state[place][1](self.t)
        return self.state[place][0]