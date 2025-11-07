import colorgram
import random
import turtle


colors = colorgram.extract('hirst_spots.jpg', 30)
# print(colors)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# print(rgb_colors)
rgb_colors = rgb_colors[2:] # remove the first two colors which are mostly background
print(rgb_colors)

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(450)
tim.setheading(0)
num_dots = 182

for dots in range(1, num_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if dots % 13 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(650)
        tim.setheading(0)




screen = turtle.Screen()
screen.exitonclick()
