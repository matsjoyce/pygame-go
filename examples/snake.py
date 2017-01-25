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

import pygame_go as pygo
import random

SNAKE_SIZE = 20

window = pygo.window(600, 400, frame_rate=5)

snake_dx, snake_dy = 0, SNAKE_SIZE
cx, cy = window.center
snake_parts = [(cx, cy - SNAKE_SIZE * i) for i in range(3)]
food_location = (random.randrange(window.width // SNAKE_SIZE) * SNAKE_SIZE,
                 random.randrange(window.height // SNAKE_SIZE) * SNAKE_SIZE)

head_image = pygo.image(SNAKE_SIZE, SNAKE_SIZE, color="white")
head_image.draw_circle(position=head_image.center, radius=2, color="black")
head_image.draw_hollow_rect(position=head_image.topleft, size=head_image.size, color="black")

tail_image_even = pygo.image(SNAKE_SIZE, SNAKE_SIZE, color="yellow")
tail_image_odd = pygo.image(SNAKE_SIZE, SNAKE_SIZE, color="green")
food_image = pygo.image(SNAKE_SIZE, SNAKE_SIZE, color="red")

while window.active():
    window.fill("white")

    for event in window.events():
        if event.is_key() and event.key in ["<Left>", "<Right>", "<Up>", "<Down>"]:
            if event.key == "<Left>" and snake_dx != SNAKE_SIZE:
                snake_dx, snake_dy = -SNAKE_SIZE, 0
            elif event.key == "<Right>" and snake_dx != -SNAKE_SIZE:
                snake_dx, snake_dy = SNAKE_SIZE, 0
            elif event.key == "<Up>" and snake_dy != SNAKE_SIZE:
                snake_dx, snake_dy = 0, -SNAKE_SIZE
            elif event.key == "<Down>" and snake_dy != -SNAKE_SIZE:
                snake_dx, snake_dy = 0, SNAKE_SIZE
            break

    if snake_parts[0] in snake_parts[1:]:
        window.draw_text(text="YOU DIED!", position=window.center, color="red", size=100, align=pygo.center)
    else:
        head_x, head_y = snake_parts[0]
        snake_parts.insert(0, ((head_x + snake_dx) % window.width,
                               (head_y + snake_dy) % window.height))
        if food_location in snake_parts:
            food_location = (random.randrange(window.width // SNAKE_SIZE) * SNAKE_SIZE,
                             random.randrange(window.height // SNAKE_SIZE) * SNAKE_SIZE)
        else:
            snake_parts.pop()

    for i, part in enumerate(snake_parts):
        if i == 0:
            window.draw_image(head_image, part)
        else:
            window.draw_image(tail_image_odd if i % 2 else tail_image_even, part)

    window.draw_image(food_image, food_location)
    window.draw_text(text="Score: {}".format(len(snake_parts) - 3), position=window.topleft, color="black")
    window.update()
