from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True

scoreboard.update_score()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision:
    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect wall collision:
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        scoreboard.game_over()
        game_is_on = False

    # Detect tail collision:
    for segments in snake.snake_segment[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
