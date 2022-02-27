#Third set of graphics

from turtle import * 
from colour_codes import yellows, greens
from shapes import tri_spiral
import random

##set background
bgcolor('black')

##draw green whirlpool
whirlpool = Turtle()
whirlpool.hideturtle()
whirlpool.speed(0)
tri_spiral(whirlpool, greens)

##draw yellow-green planet
planet2 = Turtle()
planet2.penup()
planet2.setpos(0, -220)
planet2.pendown()
planet2.hideturtle()
planet2.speed(0)
n = 110
angle = 0

planet2.seth(angle)

for i in range(1, n+1, 1):
  planet2.pencolor(random.choice(yellows + greens))
  planet2.circle(2 * i) #radius

whirlpool.clear()

for i in range(n+1, 1, -1):
  planet2.pencolor('black')
  planet2.circle(2 * i) #radius

planet2.clear()