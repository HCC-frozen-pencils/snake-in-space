## zero-G SNAKE!
import turtle
from turtle import Screen
import pygame
import random
import keyboard
import math
import time
from random import randint

wn = turtle.Screen()
wn.bgcolor("lightblue")


#food
food = turtle.Turtle(shape="circle", visible=False)
food.color('red')

def foodAppear():
  x = randint(-20, 20)
  y = randint(-20, 20)
  food.hideturtle()
  food.penup()

  food.goto(x, y)
  food.showturtle()

  

class Snake:

  def __init__(self):
    self.head = turtle.Turtle(shape = "square")
    self.snake_color = 'green'
    self.head.color(self.snake_color)
    self.head.penup()
    self.speed = 3
    
    self.direction = "stop"

    # initialize self.tail to have 0 length
    self.tail = [self.head]


    

  # momentum
  def thrust(self):
    global delay
    delay = 0.03

  def grow(self):
    new_segment = turtle.Turtle(shape = 'square')
    new_segment.color(self.snake_color)
    new_segment.penup()
    self.tail.append(new_segment)

    # replace segments with self.tail in this stolen code
    # yoinked from https://www.edureka.co/blog/python-turtle-module/#CreateSnake'sHead

    ## movement on grid
  def move(self):
    if self.direction == "up":
        y = self.head.ycor() 
        self.head.sety(y + 20)
 
    if self.direction == "down":
        y = self.head.ycor() 
        self.head.sety(y - 20)
 
    if self.direction == "right":
        x = self.head.xcor()
        self.head.setx(x + 20)
 
    if self.direction == "left":
        x = self.head.xcor()
        self.head.setx(x - 20)

    for index in range(len(self.tail)-1, 0, -1):
      x = self.tail[index-1].xcor()
      y = self.tail[index-1].ycor()
      self.tail[index].goto(x+20, y)

  def go_up(self):
    if self.direction != "down":
      self.direction = "up"
 
  def go_down(self):
    if self.direction != "up":
      self.direction = "down"
 
  def go_right(self):
    if self.direction != "left":
      self.direction = "right"
 
  def go_left(self):
    if self.direction != "right":
      self.direction = "left"
  
snek = Snake()
milk = Snake()

milk.snake_color = 'chocolate'


wn.listen()
wn.onkey(snek.go_up, 'Up')
wn.onkey(snek.go_down, 'Down')
wn.onkey(snek.go_left, 'Left')
wn.onkey(snek.go_right, 'Right')

wn.onkey(milk.go_up, 'w')
wn.onkey(milk.go_down, 's')
wn.onkey(milk.go_left, 'a')
wn.onkey(milk.go_right, 'd')

wn.onkey(snek.thrust, 'z')
wn.onkey(milk.thrust, 'q')

#milk_snake.grow()

# scoring

def snek_score():
  global score1
  score1 = score1 + 1
  print("Snek Score: " + str(score1))
  if score1 == 15:
      print ("Snek Wins!")

def milk_score():
  global score2
  score2 = score2 + 1
  print("Milk Score: " + str(score2))
  if score2 == 15:
      print ("Milk Snake Wins!")

# barriers

# if snake is at x value of 300, can't go right anymore
#if snek.head.pos == (300):


# asteroids!

class asteroids():
  asteroid = turtle.Turtle(shape = 'circle', visible = False)
  asteroid.color('gray')
  asteroid.penup()

# projectile (shoot food) 

def shoot():
  global projectile
      

wn.onkey(shoot, 'space')

# yoshi tongue

## game loop
score1 = 0
score2 = 0

foodAppear()
delay = 0.1

while score1 < 15 and score2 < 15:
    wn.update()
    snek.move()
    milk.move()
    time.sleep(delay)
    
    if food.distance(snek.head) < 18:
      food.clear()
      snek.grow()
      snek_score()
      foodAppear()
    
    if food.distance(milk.head) < 18:
      food.clear()
      milk.grow()
      milk_score()
      foodAppear()
    
    
