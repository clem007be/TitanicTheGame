# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:48:42 2023

@author: cleme
"""

import turtle as ttl
import Carte as C
import data
import random as rdm
import matplotlib.pyplot as plt
import tkinter as tk

class Map():
    class MapGUI():
        def __init__(self, cv):
            self.screen = ttl.TurtleScreen(cv)
            self.screen.bgcolor('lightblue')
            self.t = ttl.RawTurtle(self.screen)
            self.t.hideturtle()
            self.t.penup()
            self.initMap()

        def initMap(self):
            C.pontAvantDroit(self.t)
            C.pontMilieuDroit(self.t)
            C.pontArrDroit(self.t)
            C.pontAvantGauche(self.t)
            C.pontMilieuGauche(self.t)
            C.pontArrGauche(self.t)
            C.moteur(self.t)
            C.cabine(self.t)
            C.buffet(self.t)
            C.tapis(self.t)
            C.tables(self.t)
            C.chambresDroite(self.t)
            C.chambresGauche(self.t)
            C.salleSecrete(self.t)
            C.pontAvant(self.t)
            C.pontArriere(self.t)
            C.bateauDroit(self.t)
            C.bateauGauche(self.t)  
            
        def sinking(self, place,state):
            if(state == 'sinking'):
                data.places[place]['func'](self.t, sinking=True)
            if(state == 'sunk'):
                data.places[place]['func'](self.t, sunk=True)
            
    def __init__(self,cv):
        self.map = self.MapGUI(cv)
        self.state = {"pontAvantDroit":0, "pontMilieuDroit":0, "pontArrDroit":0, "pontAvantGauche":0,
                      "pontMilieuGauche":0, "pontArrGauche":0, "moteur":0, "cabine":0, "buffet":0, 
                      "tapis":0, "tables":0,"pontAvant":0, "pontArriere":0, "chambresGauche":0,
                      "chambresDroite":0, "salleSecrete":0}
        self.people = {"pontAvantDroit":-1, "pontMilieuDroit":-1, "pontArrDroit":-1, "pontAvantGauche":-1,
                      "pontMilieuGauche":-1, "pontArrGauche":-1, "moteur":-1, "cabine":-1, "buffet":-1, 
                      "tapis":-1, "tables":-1,"pontAvant":-1, "pontArriere":-1, "chambresGauche":-1,
                      "chambresDroite":-1, "salleSecrete":-1}
        
    def sinking(self, place):
        if (self.state[place] == 2):
            print("Le terrain est déjà innondé.")
        else:
            self.state[place] += 1 
            if (self.state[place] == 1):
                print("Le terrain est en train de sombrer.")
                self.map.sinking(place,'sinking')
            elif(self.state[place] == 2):
                print("Le terrain est innondé.")
                self.map.sinking(place,'sunk')
        return self.state[place]

    def set_state(self,place):
        if (self.state[place] < 2):
            self.state[place] += 1

    def get_state(self,place):
        return self.state[place]

    def add_people(self,player):
        self.people[player.place[0]] += 1
        player.set_which_pawn(self.people[player.place[0]])
        player.pion()

    def remove_people(self,player):
        self.people[player.place[0]] -=1
        player.t.clear()
        # return self.people[player.place[0]]
        

    def get_people(self,place):
        return self.people[place]
    
class Player():
    def __init__(self, map, color):
        self.t = ttl.RawTurtle(map.map.screen)
        self.t.hideturtle()
        self.t.color(color,color)
        self.t.penup()
        self.place = ["",0]
        self.tresors = 0
        self.moves = 3
        self.map = map
        self.set_place("tables")
    
    def pion(self):
        self.t.speed(0)
        self.t.goto(data.places[self.place[0]]['pos'][self.place[1]])
        self.t.seth(90)
        self.t.fd(0.25*C.SCALE)
        self.t.right(90)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(-0.25*C.SCALE)
        self.t.end_fill()
        self.t.penup()

    def set_place(self,place):
        self.place[0] = place
        self.map.add_people(self)

    def set_which_pawn(self,n):
        self.place[1] = n

    def get_position(self):
        return self.place
    
    def travel(self,place):
        self.map.remove_people(self)
        self.set_place(place)

    def get_tresors(self):
        return self.tresors

    def leave(self,map):
        if(self.place == 'bateauGauche' or self.place == 'bateauDroit'):
            map.set_state(self.place)

    def drying(self, place, map):
        if (map.state[place] == 0):
            print("Le terrain est déjà sec.")
        elif (self.state[place] == 2):
            print("Le terrain est innondé et ne peut pas être assècher.")
        else:
            print("Le terraine est asséché.")
            self.state[place] -= 1
            data.places[self.place]['func'](map.map.t)
        return self.state[place]

    def turn(self, e):
        self
        return
    
    