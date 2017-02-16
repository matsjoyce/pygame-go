"""
collide.py
==========
Move the cursor to move the red block.
If the red block touches the green block, the screen turns black.
If the black circle inside the red block touches the green circle, the screen turns red.

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

mode = 0

cursor_block = pygo.image(20, 20, color="red")

cursor_circle = pygo.image(20, 20)
cursor_circle.draw_circle(position=cursor_circle.center, radius=cursor_circle.width // 2, color="red")

collide_circle = pygo.image(100, 100)
collide_circle.draw_circle(position=collide_circle.center, radius=collide_circle.width // 2, color="green")

collide_block = pygo.image(100, 100, color="green")

while window.active():
    for event in window.events():
        if event.is_key() and event.key == " ":
            mode = (mode + 1) % 2
    position = pygo.mouse_position()
    if mode == 0 and pygo.collides_rect_rect(position_a=window.center, size_a=collide_block.size, align_a=pygo.center,
                                             position_b=position, size_b=cursor_block.size, align_b=pygo.center):
        window.fill("black")
    elif mode == 1 and pygo.collides_circle_circle(position_a=window.center, radius_a=collide_circle.width // 2,
                                                   position_b=position, radius_b=cursor_circle.width // 2):
        window.fill("black")
    else:
        window.fill("white")

    if mode == 0:
        window.draw_image(collide_block, window.center, align=pygo.center)
        window.draw_image(cursor_block, position, align=pygo.center)
    elif mode == 1:
        window.draw_image(collide_circle, window.center, align=pygo.center)
        window.draw_image(cursor_circle, position, align=pygo.center)
    window.update()
