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

# Main Game Loop

while True:
  wn.update()