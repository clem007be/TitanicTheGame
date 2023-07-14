# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import Map as M
import Player as P
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import GUI

def main():
    root = Tk()
    root.geometry('1000x630+0+0')
    root.title = "Titanic The Game"

    top_frame = Frame(root,height=30,width=1000)
    top_frame.grid(row=0,column=0)
    title_lbl = Label(top_frame,text='Titanic The Game')
    title_lbl.config(padx=350)
    title_lbl.grid(row=0,column=1)
    quit_btn = ttk.Button(top_frame, text='Quit', command=root.destroy)
    quit_btn.grid(row=0,column=2)

    plateau_frame = Frame(root, height=500, width=1000)
    plateau_frame.grid(row=1,column=0)
    canvas = Canvas(plateau_frame, height=500, width=1000)
    canvas.grid(row=0,column=0)
    plateau = M.Map(canvas)
    playerList = P.PlayerList(P.Player(plateau,'red'))
    playerList.add_player(P.Player(plateau,'blue'))
    print(P.PlayerList.length())

    button_frame = GUI.ActualizedFrame(root,playerList=playerList, height=100,width=1000)
    button_frame.grid(row=2,column=0)
    button_frame.show_buttons()
    
    root.mainloop()

    

if __name__ == "__main__":
    main()