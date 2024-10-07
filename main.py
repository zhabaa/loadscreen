"""
TODO Посмотреть можно ли через наследование улучшить класс Dot и не переопределять фукнцию move()
Линия между точками - градиент из цвета одной к другой
плавное появление \ исчезнование 
"""

import sys
import random

import pygame as pg

from settings import *
from dot import Dot


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


def main():
    pg.init()

    clock = pg.time.Clock()
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    dots = list()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and \
                event.key == pg.K_ESCAPE
            ):
                pg.quit()
                sys.exit()

        screen.fill(WHITE)
        clock.tick(FPS)

        if len(dots) < DOTS_AMOUNT:
            x, y, speed, color, angle = generate_values()
            dots.append(Dot(x, y, speed, color, angle))

        for dot in dots:
            dot.move()
            dot.draw(screen)

            if not (0 < dot.x < WIDTH) or not (0 < dot.y < HEIGHT) or (dot.x == 512):
                dots.remove(dot)

        for dot1 in dots:
            for dot2 in dots:
                if distance(dot1, dot2) < LINE_LENGHT and not (dot1 is dot2):
                    pg.draw.line(screen, color, dot1.pos(), dot2.pos())

        pg.display.flip()


if __name__ == "__main__":
    main()
