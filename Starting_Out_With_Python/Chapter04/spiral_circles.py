#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Эта программа рисует узор, используя повторяющиеся круги.
import turtle
# Именованные константы.
NUM_CIRCLES = 36  # Количество рисуемых кругов.
RADIUS = 100  # Радиус каждого круга.
ANGLE = 10  # Угол поворота.
ANIMATION_SPEED = 0  # Скорость анимации.
# Задать скорость анимации.
turtle.speed(ANIMATION_SPEED)
# Нарисовать 36 кругов, наклоняя черепаху на 10 градусов после того, как каждый круг был нарисован.
for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)
