"""
ball_bounce.py
==============
Bounce a ball around the screen. Compare this to ball_bounce_plain_pygame.py

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

BALL_RADIUS = 50

window = pygo.window(800, 600, frame_rate=60)

ball_x, ball_y = window.center
ball_dx = ball_dy = 5
bounces = 0

while window.active():
    bounced = False
    if ball_x in (BALL_RADIUS, window.width - BALL_RADIUS):
        ball_dx = -ball_dx
        bounced = True
    if ball_y in (BALL_RADIUS, window.height - BALL_RADIUS):
        ball_dy = -ball_dy
        bounced = True

    bounces += bounced
    ball_x += ball_dx
    ball_y += ball_dy

    window.fill("white")
    window.draw_circle(x=ball_x, y=ball_y, color="red", radius=BALL_RADIUS)
    window.draw_text(text="{} bounces".format(bounces), position=window.topleft, color="black")
    window.update()
