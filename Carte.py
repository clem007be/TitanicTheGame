# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:13:33 2023

@author: cleme
"""
from turtle import *
import numpy as np

SCALE = 20

def pontAvantDroit(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(-10 * SCALE, 6 * SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(6 * SCALE)
    t.rt(90)
    t.fd(2 * SCALE)
    t.rt(90)
    t.fd(6 *SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.end_fill()
    t.penup()

def pontMilieuDroit(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(-4*SCALE, 6*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(8*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(8*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.end_fill()
    t.penup()
    
def pontArrDroit(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(4*SCALE, 6*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.end_fill()
    t.penup()
    
def pontAvantGauche(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(-10*SCALE, -2*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.end_fill()
    t.penup()

def pontMilieuGauche(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(-4*SCALE, -2*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(8*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(8*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.end_fill()
    t.penup()
    
def pontArrGauche(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(4*SCALE, -2*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.end_fill()
    t.penup()

def moteur(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(-10*SCALE, 4*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(4*SCALE)
    t.rt(90)
    t.fd(4*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.lt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.end_fill()
    t.penup()

def cabine(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(-10*SCALE, 2*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.lt(90)
    t.fd(4*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(4*SCALE)
    t.end_fill()
    t.penup()

def buffet(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(-4*SCALE, 4*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.end_fill()
    t.penup()

def tapis(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(-2*SCALE, 4*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.end_fill()
    t.penup()

def tables(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(0*SCALE, 4*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(4*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(4*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.end_fill()
    t.penup()

def chambresDroite(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(4*SCALE, 4*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.end_fill()
    t.penup()

def chambresGauche(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(4*SCALE, 0)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.end_fill()
    t.penup()

def salleSecrete(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(4*SCALE, 2*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.rt(90)
    t.fd(6*SCALE)
    t.rt(90)
    t.fd(2*SCALE)
    t.end_fill()
    t.penup()

def pontAvant(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(-10*SCALE, 6*SCALE)
    t.seth(180)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.circle(8*SCALE, extent=67.97569)
    t.speed(0)
    t.penup()
    t.goto(-10*SCALE, -4*SCALE)
    t.seth(180)
    t.pendown()
    t.speed(9)
    t.circle(-8*SCALE, extent=67.97569)
    t.penup()
    t.goto(-10*SCALE, -4*SCALE)
    t.seth(90)
    t.pendown()
    t.fd(10*SCALE)
    t.end_fill()
    t.penup()

def pontArriere(t, sinking=False, sunk=False):
    t.speed(0)
    t.goto(10*SCALE, 6*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if(sinking):
        t.fillcolor('#bbbbbb')
    elif(sunk):
        t.fillcolor('black')
    else:
        t.fillcolor('#fede86')
        t.speed(9)
    t.begin_fill()
    t.circle(-5*SCALE, extent=180)
    t.rt(90)
    t.fd(10*SCALE)
    t.end_fill()
    t.penup()

def bateauDroit(t, left=False):
    t.speed(0)
    t.goto(-8*SCALE, 8*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if (left):
        t.fillcolor('black')
    else:
        t.fillcolor('#ff7f02')
        t.speed(9)
    t.begin_fill()
    t.fd(2*SCALE)
    t.circle(-1*SCALE, extent=180)
    t.fd(2*SCALE)
    t.circle(-1*SCALE, extent=180)
    t.end_fill()
    t.penup()

def bateauGauche(t, left=False):
    t.speed(0)
    t.goto(6*SCALE, -4*SCALE)
    t.seth(0)
    t.pendown()
    t.speed(0)
    if (left):
        t.fillcolor('black')
    else:
        t.fillcolor('#ff7f02')
        t.speed(9)
    t.begin_fill()
    t.fd(2*SCALE)
    t.circle(-1*SCALE, extent=180)
    t.fd(2*SCALE)
    t.circle(-1*SCALE, extent=180)
    t.end_fill()
    t.penup()