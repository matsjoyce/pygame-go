"""
snake.py
========
Play the classic snake game. Use your arrow keys to direct the snake to the red food. You will die if you hit yourself.

Copyright (C) 2017 Matthew Joyce (matsjoyce@gmail.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the Lesser GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
Lesser GNU General Public License for more details.

You should have received a copy of the Lesser GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import pygame_quick as pgq
import random

SNAKE_SIZE = 20

window = pgq.window(600, 400, frame_rate=5)

cx, cy = window.center
snake_dx, snake_dy = 0, SNAKE_SIZE
snake_dead = False
snake_parts = [(cx, cy - SNAKE_SIZE * i) for i in range(3)]
food_location = (random.randrange(window.width // SNAKE_SIZE) * SNAKE_SIZE,
                 random.randrange(window.height // SNAKE_SIZE) * SNAKE_SIZE)

head_image = pgq.image(SNAKE_SIZE, SNAKE_SIZE, color="white")
head_image.draw_circle(position=head_image.center, radius=2, color="black")
head_image.draw_hollow_rect(position=head_image.topleft, size=head_image.size, color="black")

tail_image_even = pgq.image(SNAKE_SIZE, SNAKE_SIZE, color="yellow")
tail_image_odd = pgq.image(SNAKE_SIZE, SNAKE_SIZE, color="green")
food_image = pgq.image(SNAKE_SIZE, SNAKE_SIZE, color="red")

while window.active():
    window.fill("white")
    if snake_dead:
        window.draw_text(text="Score: {}".format(len(snake_parts) - 3), position=window.topleft, color="black")
        window.draw_text(text="YOU DIED!", position=window.center, color="red", size=60, align=pgq.center)
        window.update()
        continue

    for _, key in window.events():
        if key == "<Left>" and snake_dx != SNAKE_SIZE:
            snake_dx, snake_dy = -SNAKE_SIZE, 0
        elif key == "<Right>" and snake_dx != -SNAKE_SIZE:
            snake_dx, snake_dy = SNAKE_SIZE, 0
        elif key == "<Up>" and snake_dy != SNAKE_SIZE:
            snake_dx, snake_dy = 0, -SNAKE_SIZE
        elif key == "<Down>" and snake_dy != -SNAKE_SIZE:
            snake_dx, snake_dy = 0, SNAKE_SIZE
        else:
            continue
        break

    head_x, head_y = snake_parts[0]
    head_x = (head_x + snake_dx) % window.width
    head_y = (head_y + snake_dy) % window.height
    new_snake = [(head_x, head_y)] + snake_parts[:-1]
    if food_location in new_snake:
        new_snake.append(snake_parts[-1])
        food_location = (random.randrange(window.width // SNAKE_SIZE) * SNAKE_SIZE,
                         random.randrange(window.height // SNAKE_SIZE) * SNAKE_SIZE)
    snake_parts = new_snake
    snake_dead = snake_parts[0] in snake_parts[1:]

    for i, part in enumerate(snake_parts):
        if i == 0:
            head_image.draw(window, part)
        elif i % 2:
            tail_image_odd.draw(window, part)
        else:
            tail_image_even.draw(window, part)
    food_image.draw(window, food_location)
    window.draw_text(text="Score: {}".format(len(snake_parts) - 3), position=window.topleft, color="black")
    window.update()
