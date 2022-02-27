#Second set of graphics

from turtle import * 
from colour_codes import blues, greens
from shapes import ellipse
import random

##set background
bgcolor('black')

x = 0
speed(0)
radius = 2
hideturtle()

##draw blue planet
#concentric circles
while x < 100:
  pencolor(random.choice(blues)) 
  circle(radius * x) 
  up()
  sety((radius * x) * (-1))
  down()
  x += 1

#patchy reversal
while x > 0:
  pencolor('black')
  circle(radius * x)
  up()
  sety((radius * x) * (-1))
  down()
  x -= 1

##draw blue planet rings
ring1 = Turtle()
ring1.hideturtle()
ring1.speed(0)
ring1.penup()
ring1.setpos(-180.00, -150.00)
ring1.pendown()
ring1.pensize(2)
ellipse(ring1, 330, blues, 0)

ring2 = Turtle()
ring2.hideturtle()
ring2.speed(0)
ring2.penup()
ring2.setpos(180, 150)
ring2.pendown()
ring2.pensize(2)
ellipse(ring2, 330, blues, 180)

ring1.clear()
ring2.clear()

clear()
