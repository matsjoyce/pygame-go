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

import pygame_quick

window = pygame_quick.window(600, 400)

block = pygame_quick.image(10, 10)
block.fill(pygame_quick.color.red)

while window.active():
    window.fill(pygame_quick.color.white)
    block.draw(window, pygame_quick.mouse_position(), align=pygame_quick.center)
    window.update()
