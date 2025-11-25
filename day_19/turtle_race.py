from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
all_turtles = []
is_race_on = False

for turtle_index in range(len(colors)-1):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, -100 + turtle_index * 40)
    all_turtles.append(new_turtle)

if user_bet:
 is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
              print(f"You won! {winning_color} turtle won the game..")
            else:
              print(f"You lost! {winning_color} turtle won the game..")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()