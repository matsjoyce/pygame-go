"""
shoot.py
========
Move the cursor to aim, and press space to shoot.

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

bullet = pygame_quick.image(10, 10)
bullet.draw_circle(position=bullet.center, radius=5, color="red")
bullets = []

while window.active():
    window.fill("white")
    window.draw_text(text="Press space to shoot...", position=window.topleft, color="black")

    new_bullets = []
    for x, y in bullets:
        if y > -10:
            new_bullets.append((x, y - 10))
    bullets = new_bullets

    for type, value in window.events():
        if type is pygame_quick.key_down and value == " ":
            bullet_x, _ = pygame_quick.mouse_position()
            bullets.append((bullet_x, window.height))

    for bullet_position in bullets:
        window.draw_image(bullet, bullet_position, align=pygame_quick.center)

    window.update()
