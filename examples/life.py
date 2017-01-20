"""
life.py
=======
Play Conway's Game of Life.

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
import itertools

block_size = 20

window = pgq.window(600, 400, frame_rate=10)

cells = set()
paused = False


def point_to_block(x, y):
    block_x = (x - window.width // 2) // block_size
    block_y = (y - window.height // 2) // block_size
    return block_x, block_y


def block_to_point(block_x, block_y):
    x = block_x * block_size + window.width // 2
    y = block_y * block_size + window.height // 2
    return x, y


while window.active():
    if not paused:
        new_cells = set()
        maybe_alive = cells.copy()
        checked = set()
        while maybe_alive - checked:
            x, y = (maybe_alive - checked).pop()
            checked.add((x, y))
            number_of_neighbours = -((x, y) in cells)
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if (x + i, y + j) in cells:
                        number_of_neighbours += 1
                    if (x, y) in cells:
                        maybe_alive.add((x + i, y + j))
            if number_of_neighbours == 3 or number_of_neighbours == 2 and (x, y) in cells:
                new_cells.add((x, y))
        cells = new_cells

    for type, value in window.events():
        if type is pgq.mouse_down and value.button is pgq.left_button:
            cells.add(point_to_block(*value.position))
        elif type is pgq.key_down:
            if value == " ":
                paused = not paused
            elif value in "+=":
                block_size += 1
            elif value == "-":
                block_size = max(1, block_size - 1)
            elif value == "c":
                cells.clear()
        if type is pgq.mouse_motion and value.is_pressed(pgq.left_button):
            cells.add(point_to_block(*value.start))

    blocks_x, blocks_y = window.width // block_size, window.width // block_size
    for x in range(-blocks_x // 2 - 1, blocks_x // 2 + 2):
        for y in range(-blocks_y // 2 - 1, blocks_y // 2 + 2):
            if (x, y) in cells:
                window.draw_rect(position=block_to_point(x, y), width=block_size, height=block_size, color="white")
                window.draw_hollow_rect(position=block_to_point(x, y), width=block_size, height=block_size, color="gray10")
            else:
                window.draw_rect(position=block_to_point(x, y), width=block_size, height=block_size, color="black")
                window.draw_hollow_rect(position=block_to_point(x, y), width=block_size, height=block_size, color="gray10")

    if paused:
        window.draw_text(text="Paused", position=window.topleft, color="red")
    window.update()
