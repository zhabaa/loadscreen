import pygame as pg
from math import sin, cos, radians


class Dot:
    def __init__(self, x, y, speed, color, angle):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.angle = angle

        self.speed_x = speed * sin(radians(angle))
        self.speed_y = speed * cos(radians(angle))

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def pos(self):
        return self.x, self.y

    def draw(self, surface):
        pg.draw.circle(surface, self.color, (self.x, self.y), 3)
