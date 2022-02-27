#Last set of graphics

from turtle import * 
from colour_codes import blues, purples
from shapes import star_spiral
import random

##set background
bgcolor('black')

##purple nebula
nebula = Turtle()
nebula.hideturtle()
nebula.speed(0)
nebula.setpos(-50, -40)
star_spiral(nebula, blues + purples)

nebula.clear()