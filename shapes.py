#Functions to draw shapes

from turtle import *
import random

#ELLIPSE
def ellipse(turtle, radius, colour, angle):
  for i in range(4): #num of ellipses
    turtle.seth(angle)
    turtle.pensize(1)
    turtle.pencolor(random.choice(colour))
    #draw ellipses
    for i in range(2):
      turtle.circle(radius, 90)
      turtle.circle(radius//50, 90)
    angle += 1

#SPIRAL
def spiral(turtle, colour):
  for i in range(20, 300):
    turtle.pencolor(random.choice(colour))
    turtle.speed(0)
    turtle.circle(i)
    turtle.left(355)
  turtle.dot(68, '#FFEBEE')
  turtle.dot(60, 'black')

#TRIANGLE SPIRAL
def tri_spiral(turtle, colour):
  step = 9
  while step < 350:
    turtle.pencolor(random.choice(colour))
    turtle.forward(step)
    turtle.right(120)
    turtle.right(1)
    step += 1

#SQUARE SPIRAL
def sq_spiral(turtle, colour):
  step = 0
  i = 0
  while step < 660:
    index = int(i)
    turtle.pencolor(colour[index])
    turtle.forward(step)
    turtle.left(95)
    step += 1
    i += 0.2

#STAR
def star(turtle, colour):
  for i in range(150):
    turtle.pencolor(random.choice(colour))
    
    turtle.forward(110)
    turtle.left(30)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(20)
    turtle.left(30)
    turtle.forward(20)
    turtle.right(60)
    
    turtle.penup()
    turtle.setpos(0, 0)
    turtle.pendown()
  
    turtle.right(2)
  
  turtle.clear()

#STAR SPIRAL

def star_spiral(turtle, colour):
  for i in range (0, 121):
    for j in range (0, 2):
      turtle.pencolor(random.choice(colour))
      turtle.forward(100 + i * 2)
      turtle.left(100 + j)