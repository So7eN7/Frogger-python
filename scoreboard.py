from turtle import Turtle
# Constants
FONT = ("Harrington", 24, "normal")
CENTER = (0, 0)


class Scoreboard(Turtle):  # Setting up our scoreboard
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):  # Clearing the screen so that it won't be cluttered with the score
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Level

    def level_up(self):  # Leveling up
        self.level += 1
        self.update_scoreboard()

    def gameover(self):  # Gameover message
        self.goto(CENTER)
        self.write("GAME OVER", align="center", font=FONT)