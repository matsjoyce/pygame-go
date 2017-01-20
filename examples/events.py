"""
events.py
=========
Print out all the events detected in the black window.

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

        elif type is pygame_quick.mouse_motion:
            print("Mouse moved from", value.start, "to", value.end)

        elif type is pygame_quick.key_down:
            print("Key", repr(value), "pressed")

    window.update()
