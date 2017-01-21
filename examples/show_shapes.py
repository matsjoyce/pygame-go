"""
basic.py
========
Draws a square, rectangle and circle, then sits like a duck.

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
window.fill("white")

window.draw_rect(position=(100, 100), size=(80, 80), color="red")
window.draw_hollow_rect(position=(100, 100), size=(80, 80), color="cyan", thickness=1)

window.draw_rect(position=(150, 300), size=(300, 75), color="blue")
window.draw_hollow_rect(position=(150, 300), size=(300, 75), color="yellow", thickness=10)

window.draw_circle(position=(500, 150), radius=80, color="green")
window.draw_hollow_circle(position=(500, 150), radius=80, color="magenta", thickness=20)

window.draw_ellipse(position=(300, 150), size=(50, 100), color="gray")
window.draw_hollow_ellipse(position=(300, 150), size=(50, 100), color="black", thickness=5)

window.loop_forever()
