import turtle as tr
import math as mth
import random


class Molecule:
    def __init__(self, x, y, speed, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed

    def random(self):
        self.x = self.x + random.randint(-1, 1) * self.speed
        self.y = self.y + random.randint(-1, 1) * self.speed

    def show(self):

        tr.penup()
        tr.goto(self.x, self.y - self.size / 12)
        tr.pendown()
        tr.fillcolor(self.color)
        tr.begin_fill()
        tr.circle(self.size / 4)
        tr.end_fill()

    def move(self):
        tr.color('white')
        tr.penup()
        tr.goto(self.x, self.y - self.size / 12)
        tr.pendown()
        tr.fillcolor('white')
        tr.begin_fill()
        tr.circle(self.size / 4)
        tr.end_fill()

    def nearly(self, other):
        if mth.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2) < (other.size + self.size) * 12:
            other.x += 3 * (self.size + other.size)
            self.x += 3 * (self.size + other.size)

    def __str__(self):
        return

    def __repr__(self):
        return self.__str__()

