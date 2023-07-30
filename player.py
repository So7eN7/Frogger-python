from turtle import Turtle
# Constants
STARTING_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):  # Setting up our player class
    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.color("cyan")
        self.penup()
        self.goto_start()
        self.setheading(90)  # Facing upwards

    # Move functions

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:  # If the player is at finish line return true
            return True
        else :
            return False

    def goto_start(self):  # Returning to the start
        self.goto(STARTING_POS)

