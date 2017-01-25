"""
big_demo.py
===========
A big lot of random drawing and event handling, for some basic testing of pygame-go.
Press "b" to change the background to a random color, move the mouse to have the red block follow.

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

import pygame_go
import random

window = pygame_go.window(600, 400)

background_color = pygame_go.color.colors["white"]
block_x = block_y = 50

block = pygame_go.image(10, 10)
block.fill(pygame_go.color.colors["red"])
block2 = pygame_go.image(10, 10)
block2.fill(255, 0, 255)
block3 = pygame_go.image(10, 100)
block3.fill("blue")
block4 = pygame_go.image(10, 100)
block4.fill("tomato")

while window.active():
    for event in window.events():
        print(repr(event))
        if event.is_mouse_press():
            if event.button is pygame_go.left_button:
                print("Mouse click at", event.position, "using left button")
            elif event.button is pygame_go.right_button:
                print("Mouse click at", event.position, "using right button")
            elif event.button is pygame_go.middle_button:
                print("Mouse click at", event.position, "using middle button")

        elif event.is_mouse_scroll():
            print("Mouse scroll at", event.position, "using direction", event.direction)

        elif event.is_key():
            if event.key == "<Left>":
                block_x -= 1
            elif event.key == "<Right>":
                block_x += 1
            elif event.key == "<Up>":
                block_y -= 1
            elif event.key == "<Down>":
                block_y += 1
            elif event.key == "b":
                background_color = random.choice(list(pygame_go.color.colors))
            else:
                print("Key", repr(event.key), "pressed")

    window.fill(background_color)

    window.draw_rect(color="blue", x=100, y=100, width=100, height=100)
    window.draw_hollow_rect(color="red", x=100, y=100, width=100, height=100, thickness=10)

    window.draw_rect(color="yellow", x=100, y=100, width=100, height=100, align=pygame_go.topright)
    window.draw_hollow_rect(color="green", x=100, y=100, width=100, height=100,
                            thickness=10, align=pygame_go.topright)

    window.draw_rect(color="brown", x=100, y=100, width=100, height=100, align=pygame_go.bottomleft)
    window.draw_hollow_rect(color="blue", x=100, y=100, width=100, height=100,
                            thickness=10, align=pygame_go.bottomleft)

    window.draw_rect(color="gray", x=100, y=100, width=100, height=100, align=pygame_go.bottomright)
    window.draw_hollow_rect(color="black", x=100, y=100, width=100, height=100,
                            thickness=10, align=pygame_go.bottomright)

    window.draw_circle(color="green", x=500, y=300, radius=100)

    window.draw_line(start=window.topright, end=window.bottomleft, color="brown")
    window.draw_hollow_circle(color="red", x=500, y=300, radius=100, thickness=10)

    window.draw_image(block, block_x, block_y)
    window.draw_image(block2, pygame_go.mouse_position(), align=pygame_go.center)
    window.draw_image(block3, window.center, align=pygame_go.center)
    window.draw_image(block4, (50, 20))
    window.draw_image(block4, window.bottomright, align=pygame_go.bottomright)

    window.draw_text(text=str(window.frame_number), position=window.topleft, color="black")
    window.draw_text(text=str(window.frame_number), position=window.bottomright, color="black",
                     align=pygame_go.bottomright)

    window.update()
