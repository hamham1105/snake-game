from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-20, 220)
        self.pencolor("white")
        self.hideturtle()
        self.score = 0

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(-20, 0)
        self.write("GAME OVER", False, align="center", font=('Courier', 24, 'normal'))