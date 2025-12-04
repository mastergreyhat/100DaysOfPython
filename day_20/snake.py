from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        for count in range(0,3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setx(-count*20)
            self.segment_list.append(new_segment)

    def move(self):
        for segment in range(len(self.segment_list)-1, 0, -1):
            new_x = self.segment_list[segment - 1].xcor()
            new_y = self.segment_list[segment - 1].ycor()
            self.segment_list[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # self.segment_list[0].setheading(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

