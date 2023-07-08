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

def main():
    root = Tk()
    root.geometry('1000x600+0+0')
    root.title = "Titanic The Game"

    plateau_frame = Frame(root, height=500, width=1000)
    plateau_frame.grid(row=0,column=0)
    canvas = Canvas(plateau_frame, height=500, width=1000)
    canvas.grid(row=0,column=0)
    plateau = GO.Map(canvas)
    player1 = GO.Player(plateau,'red')
    player2 = GO.Player(plateau,'blue')


    button_frame = Frame(root, height=100,width=1000)
    button_frame.grid(row=1,column=0)
    
    quit_btn = ttk.Button(root, text='Quit', command=root.quit)
    quit_btn.place(relx=1,rely=0,anchor='ne')
    root.mainloop()
    

if __name__ == "__main__":
    main()