from turtle import Screen
import time
from player import Player
from car import Car
from scoreboard import Scoreboard

# Setting up our screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Frogger")
screen.bgcolor("dark blue")
screen.tracer(0)

# Creating our game objects

player = Player()
car = Car()
scoreboard = Scoreboard()

# Getting player inputs

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

# Game loop/logic

is_game_running = True
while is_game_running:
    # Screen rendering and car spawn
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    for i in car.cars:  # Car collision with the player
        if i.distance(player) < 20:
            is_game_running = False
            scoreboard.gameover()  # If hit commence gameover

    if player.is_at_finish_line():  # If the player reached the end. Reset his position and level up
        player.goto_start()
        car.level_up()
        scoreboard.level_up()

screen.exitonclick()