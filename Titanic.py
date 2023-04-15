# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from turtle import *
from Carte import *
from GameObject import *
import matplotlib.pyplot as plt
import time
from tkinter import *
from tkinter import ttk
def main():
    root = Tk()
    root.title = "Game"
    root.resizable(0,0)
    root.wm_attributes("-topmost", 1)
    canvas = tkt.Canvas(root)
    carte = Map(canvas)
    P1 = Player(canvas,'#ff0000')
    P2 = Player(canvas,'#ff0000')
    P3 = Player(canvas,'#ff0000')
    P4 = Player(canvas,'#ff0000')
    P5 = Player(canvas,'#ff0000')
    P6 = Player(canvas,'#ff0000')
    while True:
        P1.turn()
        # P2
        
        break
    exitonclick()
    

if __name__ == "__main__":
    main()