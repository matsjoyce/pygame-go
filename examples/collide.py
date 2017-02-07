"""
collide.py
==========
Move the cursor to move the red block.
If the red block touches the black block, the screen turns black.

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

window = pygo.window(600, 400, frame_rate=60)
block = pygo.image(10, 10, color="red")
collide_block = pygo.image(100, 100, color="green")

while window.active():
    position = pygo.mouse_position()
    if pygo.collides_rect_rect(x_a=300, y_a=300, size_a=collide_block.size, align_a=pygo.center,
                               position_b=position, size_b=block.size, align_b=pygo.center):
        window.fill("black")
    else:
        window.fill("white")

    window.draw_image(collide_block, x=300, y=300, align=pygo.center)
    window.draw_image(block, position, align=pygo.center)
    window.update()
