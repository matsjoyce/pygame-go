"""
pygame-go - PyGame for Humans!
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

import pygame

from .shortcuts import with_pygame_inited, ArgumentExtractor
from . import events


@with_pygame_inited
def mouse_position():
    return pygame.mouse.get_pos()


@with_pygame_inited
def set_mouse_position(*args, **kwargs):
    ae = ArgumentExtractor(kwargs)
    pos = ae.extract_position(args=args)
    ae.finalize()
    pygame.mouse.set_pos(pos)


@with_pygame_inited
def is_key_pressed(key):
    keys = pygame.key.get_pressed()
    for const, name in events.KEY_MAPPING.items():
        if name == key and keys[const]:
            return True
    return False


@with_pygame_inited
def is_mouse_pressed(button):
    l, m, r = pygame.mouse.get_pressed()
    if button is events.Button.left:
        return bool(l)
    if button is events.Button.right:
        return bool(r)
    if button is events.Button.middle:
        return bool(m)
    return False
