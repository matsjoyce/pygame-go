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

import pygame_go

window = pygame_go.window(600, 400)

while window.active():
    for event in window.events():
        if event.is_mouse_press():
            if event.button is pygame_go.left_button:
                print("Mouse click at", event.position, "using left button")
            elif event.button is pygame_go.right_button:
                print("Mouse click at", event.position, "using right button")
            elif event.button is pygame_go.middle_button:
                print("Mouse click at", event.position, "using middle button")

        elif event.is_mouse_scroll():
            print("Mouse scroll at", event.position, "using direction", event.direction)

        elif event.is_mouse_motion():
            print("Mouse moved from", event.start, "to", event.end)

        elif event.is_key():
            print("Key", repr(event.key), "pressed")

    window.update()
