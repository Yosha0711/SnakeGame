from turtle import Turtle,Screen
import random

screen=Screen()
screen.colormode(255)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):

        # Generating random food colurs
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        self.color(r,g,b)

        # Generating food at random locations
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
