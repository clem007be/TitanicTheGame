# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:48:42 2023

@author: cleme
"""

from turtle import *
from Carte import *
import random as rdm
import matplotlib.pyplot as plt
import tkinter as tkt

class Player():
    
    places = {"pontAvantDroit":[1/2,(-7.5*SCALE,5*SCALE),(-6.5*SCALE,5*SCALE),(-8.5*SCALE,5*SCALE),(-5.5*SCALE,5*SCALE),(-9.5*SCALE,5*SCALE),(-4.5*SCALE,5*SCALE)],
              "pontMilieuDroit":[1/2,(-0.5*SCALE,5*SCALE),(0.5*SCALE,5*SCALE),(-1.5*SCALE,5*SCALE),(1.5*SCALE,5*SCALE),(-2.5*SCALE,5*SCALE),(2.5*SCALE,5*SCALE)],
              "pontArrDroit":[1/2,(7.5*SCALE,5*SCALE),(6.5*SCALE,5*SCALE),(8.5*SCALE,5*SCALE),(5.5*SCALE,5*SCALE),(9.5*SCALE,5*SCALE),(4.5*SCALE,5*SCALE)],
              "pontAvantGauche":[1/2,(-7.5*SCALE,-3*SCALE),(-6.5*SCALE,-3*SCALE),(-8.5*SCALE,-3*SCALE),(-5.5*SCALE,-3*SCALE),(-9.5*SCALE,-3*SCALE),(-4.5*SCALE,-3*SCALE)],
              "pontMilieuGauche":[1/2,(-0.5*SCALE,-3*SCALE),(0.5*SCALE,-3*SCALE),(-1.5*SCALE,-3*SCALE),(1.5*SCALE,-3*SCALE),(-2.5*SCALE,-3*SCALE),(2.5*SCALE,-3*SCALE)],
              "pontArrGauche":[1/2,(7.5*SCALE,-3*SCALE),(6.5*SCALE,-3*SCALE),(8.5*SCALE,-3*SCALE),(5.5*SCALE,-3*SCALE),(9.5*SCALE,-3*SCALE),(4.5*SCALE,-3*SCALE)],
              "moteur":[1/2,(-9*SCALE,3*SCALE),(-7*SCALE,3*SCALE),(-5*SCALE,3*SCALE),(-7*SCALE,1*SCALE),(-5*SCALE,1*SCALE),(-6*SCALE,2*SCALE)],
              "cabine":[1/2,(-7.5*SCALE,-1*SCALE),(-6.5*SCALE,-1*SCALE),(-8.5*SCALE,-1*SCALE),(-5.5*SCALE,-1*SCALE),(-9.5*SCALE,-1*SCALE),(-4.5*SCALE,-1*SCALE)], 
              "buffet":[1/2,(-3*SCALE,0.5*SCALE),(-3*SCALE,1.5*SCALE),(-3*SCALE,-0.5*SCALE),(-3*SCALE,2.5*SCALE),(-3*SCALE,-1.5*SCALE),(-3*SCALE,3.5*SCALE)],
              "tapis":[1/2,(-1*SCALE,0.5*SCALE),(-1*SCALE,1.5*SCALE),(-1*SCALE,-0.5*SCALE),(-1*SCALE,2.5*SCALE),(-1*SCALE,-1.5*SCALE),(-1*SCALE,3.5*SCALE)],
              "tables":[1/2,(1*SCALE,1*SCALE),(3*SCALE,1*SCALE),(1*SCALE,3*SCALE),(3*SCALE,3*SCALE),(1*SCALE,-1*SCALE),(3*SCALE,-1*SCALE)],
              "pontAvant":[1/2,(-11*SCALE,1*SCALE),(-11*SCALE,3*SCALE),(-11*SCALE,-1*SCALE),(-13*SCALE,2*SCALE),(-13*SCALE,0),(-15*SCALE,1*SCALE)],
              "pontArriere":[1/2,(11*SCALE,1*SCALE),(11*SCALE,3*SCALE),(11*SCALE,-1*SCALE),(13*SCALE,2*SCALE),(13*SCALE,0),(15*SCALE,1*SCALE)],
              "chambresGauche":[1/2,(7.5*SCALE,3*SCALE),(6.5*SCALE,3*SCALE),(8.5*SCALE,3*SCALE),(5.5*SCALE,3*SCALE),(9.5*SCALE,3*SCALE),(4.5*SCALE,3*SCALE)],
              "chambresDroite":[1/2,(7.5*SCALE,-1*SCALE),(6.5*SCALE,-1*SCALE),(8.5*SCALE,-1*SCALE),(5.5*SCALE,-1*SCALE),(9.5*SCALE,-1*SCALE),(4.5*SCALE,-1*SCALE)],
              "salleSecrete":[1/2,(7.5*SCALE,1*SCALE),(6.5*SCALE,1*SCALE),(8.5*SCALE,1*SCALE),(5.5*SCALE,1*SCALE),(9.5*SCALE,1*SCALE),(4.5*SCALE,1*SCALE)]}
    
    def __init__(self,cv, color):
        self.t = RawTurtle(cv)
        self.t.hideturtle()
        self.t.color(color,color)
        self.place = "tables"
        self.tresors = 0
        self.move = 3
        # self
        
    def pion(self, n):
        self.t.speed(0)
        self.t.penup()
        self.t.goto(Player.places[self.place][n])
        self.t.seth(90)
        self.t.fd(0.25*SCALE)
        self.t.right(90)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(-0.25*SCALE)
        self.t.end_fill()
    
    def set_place(self,place):
        self.place = place
    
    def get_tresors(self):
        return self.tresors
    
    def turn(self):
        self
        return
        
class Map():
    def __init__(self,cv):
        self.t = RawTurtle(cv)
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