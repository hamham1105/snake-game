from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake_length = 3
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]

    def create_snake(self):
        x = 0
        for seg_index in range(0, self.snake_length):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=x, y=0)
            self.snake_segment.append(new_segment)
            x -= 20

    def move(self):
        for seg_num in range(self.snake_length - 1, 0, -1):
            new_x = self.snake_segment[seg_num - 1].xcor()
            new_y = self.snake_segment[seg_num - 1].ycor()
            self.snake_segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE )

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

