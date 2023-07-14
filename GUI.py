# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from Player import *
import data


class ActualizedButton():
    def __init__(self, master, player:Player) -> None:
        self._master = master
        self._player = player
        self._button = ttk.Button(master.frame)
    
    def grid(self,row:int,column:int) -> None:
        self._button.grid(row=row,column=column)

    def destroy(self):
        self._button.destroy()

    def travel(self,place:str) -> None:
        self._button.config(text=place)
        def func(e):
            self._player.travel(place)
            self._master.after(1, self._master.show_buttons)
        self._button.bind('<1>',func)
        
    def drying(self,place:str) -> None:
        self._button.config(text=place)
        def func(e):
            self._player.drying(place)
            self._master.after(1, self._master.show_buttons)
        self._button.bind('<1>',func)

    def search(self, place:str) -> None:
        self._button.config(text='Search')
        # def func(e):
        #     self._player.search(place)
        #     self._master.after(1, self._master.show_buttons)
        # self._button.bind('<1>', func)

class ActualizedFrame():
    def __init__(self,master,playerList:PlayerList,height:int,width:int) -> None:
        self._master = master
        self._playerList = playerList
        self._frame = tk.Frame(master,height=height,width=width)
        self._items = []
    
    @property
    def frame(self) -> tk.Frame:
        return self._frame
                
    @property
    def playerList(self) -> PlayerList:
        return self._playerList
    
    @playerList.setter
    def playerList(self, playerList:PlayerList) -> None:
        self._playerList = playerList
        
    def after(self, time:int, func):
        for i in self._items: i.destroy()
        self._frame.after(time,func)  

    def grid(self, row:int, column:int):
        self._frame.grid(row=row,column=column)

    def show_buttons(self) -> None:
        if (self.playerList.player.moves <= 0):
            self._playerList.player.moves = 3
            self._playerList = self._playerList.next
        player = self.playerList.player
        self.travel_buttons(player)
        self.drying_buttons(player)

    def travel_buttons(self,player:Player) -> None:
        lbl = ttk.Label(self._frame,text='Travel')
        lbl.grid(row=0,column=0)
        self._items.append(lbl)
        j = tk.IntVar()
        j.set(1)
        for i in data.places[player.get_place()]['border']:
            button = ActualizedButton(self,player)
            button.travel(i)
            button.grid(row=0,column=j.get())
            self._items.append(button)
            j.set(j.get() + 1)

    def drying_buttons(self, player:Player) -> None:
        lbl = ttk.Label(self._frame,text='Dry out')
        lbl.grid(row=1,column=0)
        self._items.append(lbl)
        button = ActualizedButton(self,player)
        button.drying(player.get_place())
        button.grid(row=1,column=1)
        self._items.append(button)
        j = tk.IntVar()
        j.set(2)
        for i in data.places[player.get_place()]['border']:
            button = ActualizedButton(self,player)
            button.drying(i)
            button.grid(row=1,column=j.get())
            self._items.append(button)
            j.set(j.get() + 1)

    def action_buttons(self, player:Player) -> None:
        lbl = ttk.Label(self._frame,text='Action')
        lbl.grid(row=2,column=0)
        self._items.append(lbl)
        button = ActualizedButton(self, player)
        button.search(player.get_place())
        button.grid(row=2,column=1)
        self._items.append(button)




        

        
