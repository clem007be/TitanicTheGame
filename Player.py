# -*- coding: utf-8 -*-

import Map as M
import turtle as ttl
import tkinter as tk
import data
import Carte as C

class Player:
    def __init__(self, map:M.Map, color:str) -> None:
        self.t = ttl.RawTurtle(map.map.screen)
        self.t.hideturtle()
        self.t.color(color,color)
        self.t.penup()
        self.place = [tk.StringVar(value=''),tk.IntVar(value=0)]
        self._tresors = tk.IntVar(value=0)
        self._moves = tk.IntVar(value=3)
        self.map = map
        self.set_place("tables")
    
    @property
    def moves(self) -> int:
        return self._moves.get()
    
    @moves.setter
    def moves(self,value:int) -> None:
        self._moves.set(value)

    @property
    def tresors(self) -> int:
        return self._tresors.get()
    
    @tresors.setter
    def tresors(self,value:int) -> None:
        self._tresors.set(value)

    def pion(self) -> None:
        self.t.speed(0)
        self.t.goto(data.places[self.place[0].get()]['pos'][self.place[1].get()])
        self.t.seth(90)
        self.t.fd(0.25*C.SCALE)
        self.t.right(90)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(-0.25*C.SCALE)
        self.t.end_fill()
        self.t.penup()
    
    def set_place(self,place:str) -> None:
        self.place[0].set(place)
        self.map.add_people(self)

    def set_which_pawn(self,n:int) -> None:
        self.place[1].set(n)

    def get_place(self) -> str:
        return self.place[0].get()
    
    def travel(self,place:str) -> None:
        self.map.remove_people(self)
        self.set_place(place)
        self.moves -= 1

    # def leave(self,map:Map) -> None:
    #     if(self.place[0].get() == 'bateauGauche' or self.place[0].get() == 'bateauDroit'):
    #         map.set_state(self.place[0].get())

    def drying(self, place:str) -> int:
        if (self.map.state[place].get() == 0):
            print("Le terrain est déjà sec.")
        elif (self.map.state[place].get() == 2):
            print("Le terrain est innondé et ne peut pas être assècher.")
        else:
            print("Le terraine est asséché.")
            self.map.state[place].set(self.state[place] - 1)
            data.places[self.place]['func'](map.map.t)
            self.moves.set(self.moves.get() - 1)
        return self.map.state[place].get()
    

class PlayerList:
    number = 0
    def __init__(self,player:Player, next=None) -> None:
        self._player = player
        self._next = next if (next!=None) else self
        PlayerList.number+=1
    
    @property
    def player(self) -> Player:
        return self._player
    
    @property
    def next(self):
        return self._next

    @staticmethod
    def length() -> int:
        return PlayerList.number
    
    def add_player(self, player:Player) -> None:
        node = self
        while (node._next != self):
            node = self._next
        node._next = PlayerList(player,self)
        
