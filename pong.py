import turtle
import os

# Building Screen

wn = turtle.Screen()
wn.title('Pong by Alonso')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Main Game Loop

while True:
  wn.update()