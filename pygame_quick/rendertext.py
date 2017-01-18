"""
pygame-quick - A simplified version of pygame for use in teaching
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

import functools
import pygame

from .shortcuts import with_pygame_inited


@with_pygame_inited
@functools.lru_cache(None)
def all_fonts():
    return pygame.font.get_fonts()


@with_pygame_inited
@functools.lru_cache(None)
def get_font(size, name=None, bold=False, italic=False):
    if name is None:
        fname = pygame.font.get_default_font()
    elif name not in all_fonts():
        raise ValueError("Unknown font, choose from {}".format(", ".join(all_fonts())))
    else:
        fname = pygame.font.match_font(name, bold, italic)
    return pygame.font.Font(fname, size)
