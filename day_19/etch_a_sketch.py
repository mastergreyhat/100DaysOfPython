from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def rotate_left():
    tim.left(10)

def rotate_right():
    tim.right(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(rotate_left, "a")
screen.onkey(rotate_right, "d")
screen.onkey(clear_drawing, "space")

screen.exitonclick()