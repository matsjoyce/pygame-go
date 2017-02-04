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

import pygame_go

window = pygame_go.window(600, 400)

window.draw_rect(position=(70, 70), size=(80, 80), color="red")
window.draw_hollow_rect(position=(70, 70), size=(80, 80), color="cyan", thickness=1)

window.draw_rect(position=(250, 300), size=(300, 75), color="blue")
window.draw_hollow_rect(position=(250, 300), size=(300, 75), color="yellow", thickness=10)

window.draw_circle(position=(500, 150), radius=80, color="green")
window.draw_hollow_circle(position=(500, 150), radius=80, color="magenta", thickness=20)

window.draw_ellipse(position=(300, 150), size=(50, 100), color="gray")
window.draw_hollow_ellipse(position=(300, 150), size=(50, 100), color="black", thickness=5)

window.draw_polygon([(20, 20), (40, 20), (50, 37), (40, 54), (20, 54), (10, 37)], color="tomato")
window.draw_hollow_polygon([(20, 20), (40, 20), (50, 37), (40, 54), (20, 54), (10, 37)], color="brown", thickness=2)

window.draw_line(start=(50, 50), end=(200, 40), color="green", thickness=10)

window.draw_arc(start_angle=0, end_angle=90, size=(150, 125), position=(100, 300), color="green", thickness=5)
window.draw_arc(start_angle=90, end_angle=180, size=(150, 125), position=(100, 300), color="red", thickness=5)
window.draw_arc(start_angle=180, end_angle=270, size=(150, 125), position=(100, 300), color="blue", thickness=5)
window.draw_arc(start_angle=270, end_angle=360, size=(150, 125), position=(100, 300), color="black", thickness=5)

window.loop_forever()
