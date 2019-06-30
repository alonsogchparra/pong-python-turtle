import turtle
import os

# Building Screen

wn = turtle.Screen()
wn.title('Pong by Alonso')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Global Elements

paddle_a = turtle.Turtle()
paddle_b = turtle.Turtle()
pen = turtle.Turtle()
set_goal= turtle.Turtle()
ball = turtle.Turtle()
ball.dx = 0
ball.dy = 0
score_a = 0
score_b = 0
player_a_wins = turtle.Turtle()
player_b_wins = turtle.Turtle()

# Start Game
start_game = turtle.Turtle()
start_game.speed(0)
start_game.color('white')
start_game.penup()
start_game.hideturtle()
start_game.goto(0,0)
start_game.write('PONG GAME', align='center', font=('Courier', '72', 'bold'))

# Press Enter to Start
press_enter = turtle.Turtle()
press_enter.speed(0)
press_enter.color('white')
press_enter.penup()
press_enter.hideturtle()
press_enter.goto(0, -50)
press_enter.write('Start Game (Press Enter)', align='center', font=('Courier', '36', 'bold'))

# Press Q To Exit

press_q = turtle.Turtle()
press_q.speed(0)
press_q.color('white')
press_q.penup()
press_q.hideturtle()
press_q.goto(0, -100)
press_q.write('Exit (Press Q)', align='center', font=('Courier', '36', 'bold'))

# Functions

def btn_start_pressed():

  start_game.clear()
  press_enter.clear()
  press_q.clear()
  player_a_wins.clear()
  player_b_wins.clear()

  ball.dx = 2
  ball.dy = -2

  # Paddle A

  paddle_a.speed(0)
  paddle_a.shape('square')
  paddle_a.color('white')
  paddle_a.shapesize(stretch_wid=5, stretch_len=1)
  paddle_a.penup()
  paddle_a.goto(-350, 0)

  # Paddle B

  paddle_b.speed(0)
  paddle_b.shape('square')
  paddle_b.color('white')
  paddle_b.shapesize(stretch_wid=5, stretch_len=1)
  paddle_b.penup()
  paddle_b.goto(350, 0)

  # Ball

  ball.speed(0)
  ball.shape('square')
  ball.color('white')
  ball.penup()
  ball.goto(0, 0)

  # Pen
  pen.speed(0)
  pen.color('white')
  pen.penup()
  pen.hideturtle()
  pen.goto(0, 260)
  pen.write('Player A: 0  Player B: 0', align='center', font=('Courier', 24, 'normal'))

  # Set Goal
  set_goal.speed(0)
  set_goal.color('white')
  set_goal.penup()
  set_goal.hideturtle()
  set_goal.goto(0, 250)
  set_goal.write('Reach 5 points to WIN!', align='center', font=('Courier', 10, 'normal'))



# Keyboard Binding

wn.listen()
wn.onkeypress(btn_start_pressed, 'Return')

# Main Game Loop

while True:
  wn.update()