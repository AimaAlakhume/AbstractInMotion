#Fourth set of graphics

from turtle import * 
from colour_codes import *
from shapes import star, spiral
import random

##set background
bgcolor('black')

##sun
#drawing
sun = Turtle()
sun.hideturtle()
sun.speed(0)
sun.pensize(1.3)
star(sun, yellows + oranges)
    
##red black hole
#drawing
blackhole = Turtle()
blackhole.hideturtle()
spiral(blackhole, oranges + reds)

#erasure
blackhole.speed(0)

for j in range(69, 800, 10):
  blackhole.dot(j, 'black')
blackhole.clear()