# -*- coding: utf-8 -*-
from Carte import *

places = {  
    "pontAvantDroit":{  "loot":1/2,
                        "pos":[(-7.5*SCALE,5*SCALE),(-6.5*SCALE,5*SCALE),(-8.5*SCALE,5*SCALE),(-5.5*SCALE,5*SCALE),(-9.5*SCALE,5*SCALE),(-4.5*SCALE,5*SCALE)],
                        "func":pontAvantDroit,
                        "border":["pontAvant","moteur","pontMilieuDroit","bateauDroit"]},
    "pontMilieuDroit":{ "loot":1/2,
                        "pos":[(-0.5*SCALE,5*SCALE),(0.5*SCALE,5*SCALE),(-1.5*SCALE,5*SCALE),(1.5*SCALE,5*SCALE),(-2.5*SCALE,5*SCALE),(2.5*SCALE,5*SCALE)],
                        "func":pontMilieuDroit,
                        "border":["pontAvantDroit","tapis","tables","pontArrDroit"]},
    "pontArrDroit":{    "loot":1/2,
                        "pos":[(7.5*SCALE,5*SCALE),(6.5*SCALE,5*SCALE),(8.5*SCALE,5*SCALE),(5.5*SCALE,5*SCALE),(9.5*SCALE,5*SCALE),(4.5*SCALE,5*SCALE)],
                        "func":pontArrDroit,
                        "border":["pontMilieuDroit","chambresDroite","pontArriere"]},
    "pontAvantGauche":{ "loot":1/2,
                        "pos":[(-7.5*SCALE,-3*SCALE),(-6.5*SCALE,-3*SCALE),(-8.5*SCALE,-3*SCALE),(-5.5*SCALE,-3*SCALE),(-9.5*SCALE,-3*SCALE),(-4.5*SCALE,-3*SCALE)],
                        "func":pontAvantGauche,
                        "border":["pontAvant","pontMilieuGauche","cabine"]},
    "pontMilieuGauche":{"loot":1/2,
                        "pos":[(-0.5*SCALE,-3*SCALE),(0.5*SCALE,-3*SCALE),(-1.5*SCALE,-3*SCALE),(1.5*SCALE,-3*SCALE),(-2.5*SCALE,-3*SCALE),(2.5*SCALE,-3*SCALE)],
                        "func":pontMilieuGauche,
                        "border":["pontAvantGauche","tapis","tables","pontArrGauche"]},
    "pontArrGauche":{   "loot":1/2,
                        "pos":[(7.5*SCALE,-3*SCALE),(6.5*SCALE,-3*SCALE),(8.5*SCALE,-3*SCALE),(5.5*SCALE,-3*SCALE),(9.5*SCALE,-3*SCALE),(4.5*SCALE,-3*SCALE)],
                        "func":pontArrGauche,
                        "border":["pontMilieuGauche","chambresGauche","bateauGauche","pontArriere"]},
    "moteur":{          "loot":1/2,
                        "pos":[(-9*SCALE,3*SCALE),(-7*SCALE,3*SCALE),(-5*SCALE,3*SCALE),(-7*SCALE,1*SCALE),(-5*SCALE,1*SCALE),(-6*SCALE,2*SCALE)],
                        "func":moteur,
                        "border":["pontAvantDroit"]},
    "cabine":{          "loot":1/2,
                        "pos":[(-7.5*SCALE,-1*SCALE),(-6.5*SCALE,-1*SCALE),(-8.5*SCALE,-1*SCALE),(-5.5*SCALE,-1*SCALE),(-9.5*SCALE,-1*SCALE),(-4.5*SCALE,-1*SCALE)],
                        "func":cabine,
                        "border":["pontAvantGauche"]}, 
    "buffet":{          "loot":1/2,
                        "pos":[(-3*SCALE,0.5*SCALE),(-3*SCALE,1.5*SCALE),(-3*SCALE,-0.5*SCALE),(-3*SCALE,2.5*SCALE),(-3*SCALE,-1.5*SCALE),(-3*SCALE,3.5*SCALE)],
                        "func":buffet,
                        "border":["tapis"]},
    "tapis":{           "loot":1/2,
                        "pos":[(-1*SCALE,0.5*SCALE),(-1*SCALE,1.5*SCALE),(-1*SCALE,-0.5*SCALE),(-1*SCALE,2.5*SCALE),(-1*SCALE,-1.5*SCALE),(-1*SCALE,3.5*SCALE)],
                        "func":tapis,
                        "border":["buffet","pontMilieuDroit","tables","pontMilieuGauche"]},
    "tables":{          "loot":1/2,
                        "pos":[(1*SCALE,1*SCALE),(3*SCALE,1*SCALE),(1*SCALE,3*SCALE),(3*SCALE,3*SCALE),(1*SCALE,-1*SCALE),(3*SCALE,-1*SCALE)],
                        "func":tables,
                        "border":["tapis","pontMilieuDroit","pontMilieuGauche"]},
    "pontAvant":{       "loot":1/2,
                        "pos":[(-11*SCALE,1*SCALE),(-11*SCALE,3*SCALE),(-11*SCALE,-1*SCALE),(-13*SCALE,2*SCALE),(-13*SCALE,0),(-15*SCALE,1*SCALE)],
                        "func":pontAvant,
                        "border":["pontAvantDroit","pontAvantGauche"]},
    "pontArriere":{     "loot":1/2,
                        "pos":[(11*SCALE,1*SCALE),(11*SCALE,3*SCALE),(11*SCALE,-1*SCALE),(13*SCALE,2*SCALE),(13*SCALE,0),(15*SCALE,1*SCALE)],
                        "func":pontArriere,
                        "border":["pontArrDroit","pontArrGauche"]},
    "chambresDroite":{  "loot":1/2,
                        "pos":[(7.5*SCALE,3*SCALE),(6.5*SCALE,3*SCALE),(8.5*SCALE,3*SCALE),(5.5*SCALE,3*SCALE),(9.5*SCALE,3*SCALE),(4.5*SCALE,3*SCALE)],
                        "func":chambresGauche,
                        "border":["pontArrDroite"]},
    "chambresGauche":{  "loot":1/2,
                        "pos":[(7.5*SCALE,-1*SCALE),(6.5*SCALE,-1*SCALE),(8.5*SCALE,-1*SCALE),(5.5*SCALE,-1*SCALE),(9.5*SCALE,-1*SCALE),(4.5*SCALE,-1*SCALE)],
                        "func":chambresDroite,
                        "border":["pontArrGauche"]},
    "salleSecrete":{    "loot":1/2,
                        "pos":[(7.5*SCALE,1*SCALE),(6.5*SCALE,1*SCALE),(8.5*SCALE,1*SCALE),(5.5*SCALE,1*SCALE),(9.5*SCALE,1*SCALE),(4.5*SCALE,1*SCALE)],
                        "func":salleSecrete,
                        "border":['moteur']},
    "bateauDroit":{     "loot":0,
                        "pos":[(),()],
                        "func":bateauDroit,
                        "border":["pontAvantDroit"]},
    "bateauGauche":{    "loot":0,
                        "pos":[(),()],
                        "func":bateauGauche,
                        "border":["pontArrGauche"]}
}
    