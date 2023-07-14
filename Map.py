# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:48:42 2023

@author: cleme
"""

import turtle as ttl
import Carte as C
import data
import random as rdm
import tkinter as tk

class Map:
    class MapGUI:
        def __init__(self, cv:tk.Canvas):
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
            
        def sinking(self,place:str,state:str):
            if(state == 'sinking'):
                data.places[place]['func'](self.t, sinking=True)
            if(state == 'sunk'):
                data.places[place]['func'](self.t, sunk=True)
            
    def __init__(self,cv:tk.Canvas):
        self.map = self.MapGUI(cv)
        self.state = {}
        self.people = {}
        for i in data.places:
            self.state[i] = tk.IntVar(value=0)
            self.people[i] = tk.IntVar(value=-1)
    
    def sinking(self, place:str) -> int:
        if (self.state[place].get() == 2):
            print("Le terrain est déjà innondé.")
        else:
            self.state[place].set(self.state[place].get()+1)
            if (self.state[place].get() == 1):
                print("Le terrain est en train de sombrer.")
                self.map.sinking(place,'sinking')
            elif(self.state[place].get() == 2):
                print("Le terrain est innondé.")
                self.map.sinking(place,'sunk')
        return self.state[place].get()

    def set_state(self,place:str) -> None:
        if (self.state[place].get() < 2):
            self.state[place].set(self.state[place].get() + 1)

    def get_state(self,place:str) -> int:
        return self.state[place].get()

    def add_people(self,player) -> None:
        self.people[player.place[0].get()].set(self.people[player.place[0].get()].get() + 1)
        player.set_which_pawn(self.people[player.place[0].get()].get())
        player.pion()

    def remove_people(self,player) -> int:
        self.people[player.place[0].get()].set(self.people[player.place[0].get()].get() + 1)
        player.t.clear()
        return self.people[player.place[0].get()].get()
        

    def get_people(self,place:str) -> int:
        return self.people[place].get()

    
        
