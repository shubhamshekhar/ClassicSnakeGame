from turtle import Turtle
import time
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, 260)
        time.sleep(2)
        exit(0)

    def snake_dead(self, lives_left):
        self.goto(0, 0)
        if lives_left < 0:
            self.game_over()
        elif lives_left == 0:
            self.write(f"LAST CHANCE ", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"You have {lives_left + 1} lives left ", align=ALIGNMENT, font=FONT)
        self.goto(0, 260)
        time.sleep(2)
        self.reset()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt", "r") as f:
            self.high_score = int(f.read())

    def set_high_score(self):
        with open("data.txt", "w") as f:
            f.write(str(self.high_score))
