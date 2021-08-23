## zero-G SNAKE!
import turtle
from random import randint

wn = turtle.Screen()
wn.bgcolor("lightblue")

# snake
snek = turtle.Turtle()

# To make it easier to see the turtle, let's make it a shape!
snek.shape('square')

## movement on grid
speed = 1
snek.penup()
def up():
    snek.setheading(90)
def down():
    snek.setheading(270)
    
def left():
    snek.setheading(180)

def right():
    snek.setheading(0)

wn.listen()
wn.onkey(up, 'Up')
wn.onkey(down, 'Down')
wn.onkey(left, 'Left')
wn.onkey(right, 'Right')

#food
food = turtle.Turtle()
food.shape('circle')
food.color('red')

def foodAppear():
  food.penup()
  food.goto(randint(-70,70),randint(-70,70))

foodAppear()

# grow snake

# scoring

# momentum

# barriers

# asteroids!

# projectile (shoot food)

# yoshi tongue



while True:
    snek.forward(speed)
    if food.distance(snek) < 18:
      food.clear()
      foodAppear()



      
