from turtle import Turtle, Screen
import random, turtle


# color = ["red", "green", "black", "orange", "blue", "indigo", "violet", "pink", "cyan", "magenta"]
directions = [0, 90, 180, 270]
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim = Turtle()
tim.pensize(10)
tim.speed("fastest")

for _ in range(200):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()