"""
follow.py
=========
Move the cursor, and the red block follows.

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

window = pygo.window(600, 400)
block = pygo.image(10, 10, color="red")

while window.active():
    window.fill("white")
    window.draw_image(block, pygo.mouse_position(), align=pygo.center)
    window.update()
