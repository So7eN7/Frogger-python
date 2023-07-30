from turtle import Turtle
import random
# Constants
COLORS = ["red", "purple", "yellow", "green", "orange", "light blue"]
STARTING_SPEED = 5
SPEED_INCREMENT = 10


class Car:
    def __init__(self):  # Setting up our cars
        self.cars = []
        self.speed = STARTING_SPEED

    def create_cars(self):  # Creating the cars
        spawn_rate = random.randint(1, 6)  # 1 in 6 chance of spawn rate
        if spawn_rate == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)  # Adding the cars to the list of cars we set

    def move_cars(self):  # Moving cars across the screen
        for i in self.cars:
            i.backward(STARTING_SPEED)

    def level_up(self):  # If the player has leveled up we increase the speed of the cars
        self.speed += SPEED_INCREMENT