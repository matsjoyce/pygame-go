"""
big_demo.py
===========
A big lot of random drawing and event handling, for some basic testing of pygame-quick.
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

import pygame_quick
import random

window = pygame_quick.window(600, 400)

background_color = pygame_quick.color.white
block_x = block_y = 50

block = pygame_quick.image(10, 10)
block.fill(pygame_quick.color.red)
block2 = pygame_quick.image(10, 10)
block2.fill(255, 0, 255)
block3 = pygame_quick.image(10, 100)
block3.fill("blue")
block4 = pygame_quick.image(10, 100)
block4.fill("tomato")

while window.active():
    for type, value in window.events():
        if type is pygame_quick.mouse_down:
            if value.button is pygame_quick.left_button:
                print("Mouse click at", value.position, "using left button")
            elif value.button is pygame_quick.right_button:
                print("Mouse click at", value.position, "using right button")
            elif value.button is pygame_quick.middle_button:
                print("Mouse click at", value.position, "using middle button")
            elif value.is_scroll():
                print("Mouse scroll at", value.position, "using direction", value.scroll_direction)

        elif type is pygame_quick.key_down:
            if value == "<Left>":
                block_x -= 1
            elif value == "<Right>":
                block_x += 1
            elif value == "<Up>":
                block_y -= 1
            elif value == "<Down>":
                block_y += 1
            elif value == "b":
                background_color = random.choice(list(pygame_quick.color.colors))
            else:
                print("Key", repr(value), "pressed")

    window.fill(background_color)

    window.draw_rect(color="blue", x=100, y=100, width=100, height=100)
    window.draw_hollow_rect(color="red", x=100, y=100, width=100, height=100, thickness=10)

    window.draw_rect(color="yellow", x=100, y=100, width=100, height=100, align=pygame_quick.topright)
    window.draw_hollow_rect(color="green", x=100, y=100, width=100, height=100,
                            thickness=10, align=pygame_quick.topright)

    window.draw_rect(color="brown", x=100, y=100, width=100, height=100, align=pygame_quick.bottomleft)
    window.draw_hollow_rect(color="blue", x=100, y=100, width=100, height=100,
                            thickness=10, align=pygame_quick.bottomleft)

    window.draw_rect(color="gray", x=100, y=100, width=100, height=100, align=pygame_quick.bottomright)
    window.draw_hollow_rect(color="black", x=100, y=100, width=100, height=100,
                            thickness=10, align=pygame_quick.bottomright)

    window.draw_circle(color="green", x=500, y=300, radius=100)

    window.draw_line(start=window.topright, end=window.bottomleft, color="brown")
    window.draw_hollow_circle(color="red", x=500, y=300, radius=100, thickness=10)

    window.draw_image(block, block_x, block_y)
    window.draw_image(block2, pygame_quick.mouse_position(), align=pygame_quick.center)
    window.draw_image(block3, window.center, align=pygame_quick.center)
    window.draw_image(block4, (50, 20))
    window.draw_image(block4, window.bottomright, align=pygame_quick.bottomright)

    window.draw_text(text=str(window.frame_number), position=window.topleft, color=pygame_quick.color.black)
    window.draw_text(text=str(window.frame_number), position=window.bottomright, color=pygame_quick.color.black,
                     align=pygame_quick.bottomright)

    window.update()
