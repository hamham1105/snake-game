from turtle import Turtle

INITIAL_LENGTH = 10
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]
        self.tail = self.snake_segment[-1]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segment.append(new_segment)

    def create_snake(self):
        x = 0
        for seg_index in range(0, INITIAL_LENGTH):
            self.add_segment((x, 0))
            x -= 20

    def extend(self):
        self.add_segment(self.tail.position())

    def move(self):
        for seg_num in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[seg_num - 1].xcor()
            new_y = self.snake_segment[seg_num - 1].ycor()
            self.snake_segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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
