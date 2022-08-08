from turtle import Turtle
from random import randint
class Food(Turtle):

    def __init__(self):
        super().__init__()

    def generate_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6,stretch_wid=0.6)
        self.color("pink")
        self.goto(randint(-375,375),randint(-375,375))



