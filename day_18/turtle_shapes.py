from turtle import Turtle, Screen

tim = Turtle()
color = ["red", "green", "black", "orange", "blue", "indigo", "violet", "pink", "cyan", "magenta"]
for num_sides in range(3, 11):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.pencolor(color[num_sides - 3])
        tim.forward(100)
        tim.right(angle)


screen = Screen()
screen.exitonclick()