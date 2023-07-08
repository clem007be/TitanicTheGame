# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import turtle as ttl
import Carte
import GameObject as GO
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import time

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
    plateau = GO.Map(canvas)
    player1 = GO.Player(plateau,'red')

    button_frame = Frame(root, height=100,width=1000)
    button_frame.grid(row=2,column=0)
    button = ttk.Button(button_frame,text='move')
    button.bind('<1>',lambda e:player1.travel('pontMilieuGauche'))
    button.pack()
    
    root.mainloop()

    

if __name__ == "__main__":
    main()