#Last set of graphics

from turtle import * 
from colour_codes import *
from shapes import sq_spiral
import random

##set background
bgcolor('black')

##rainbow nebula
rainbow = Turtle()
rainbow.hideturtle()
rainbow.speed(0)
colours = reds+oranges+yellows+greens+blues+purples
sq_spiral(rainbow, colours)

rainbow.clear()