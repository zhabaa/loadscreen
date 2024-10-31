import sys
import random

import pygame as pg


def generate_values():
    x = random.randint(0, 1024)
    y = random.randint(0, 720)
    speed = random.randint(1, 3)
    # color = [random.randint(0, 255) for _ in range(3)]
    angle = random.randint(0, 360)

    return x, y, speed, (0, 0, 0), angle


def distance(dot1, dot2):
    dx = abs(dot1.x - dot2.x)
    dy = abs(dot1.y - dot2.y)

    return (dx * dx + dy * dy) ** 0.5


def isExit(event):
    return event.type == pg.QUIT or (
        event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
    )
