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

import pygame

from . import shortcuts


def color_clamp(value):
    return int(value) % 256


class color:
    def __init__(self, *args, **kwargs):
        ae = shortcuts.ArgumentExtractor(kwargs)
        self._color = ae.extract_color(args=args)
        ae.finalize()

    @classmethod
    def fromhex(cls, value):
        if value.startswith("#"):
            value = value[1:]
        if len(value) in (3, 4):
            value = "".join(i + i for i in value)
        if len(value) not in (6, 8):
            raise ValueError("The color is the wrong length")
        chunks = [value[i * 2:(i + 1) * 2] for i in range(len(value) // 2)]
        try:
            chunks = [int(i, 16) for i in chunks]
        except:
            raise ValueError("The color must be in hexadecimal")
        return cls(*chunks)

    @property
    def r(self):
        return self._color[0]

    @r.setter
    def r(self, value):
        self._color[0] = color_clamp(value)

    @property
    def g(self):
        return self._color[1]

    @g.setter
    def g(self, value):
        self._color[1] = color_clamp(value)

    @property
    def b(self):
        return self._color[2]

    @b.setter
    def b(self, value):
        self._color[2] = color_clamp(value)

    @property
    def transparency(self):
        return self._color[3]

    @transparency.setter
    def transparency(self, value):
        self._color[3] = color_clamp(value)

    @property
    def color(self):
        return tuple(self._color)

    @property
    def hex(self):
        if self._colors[3] == 255:
            return "#" + ("{:02x}" * 3).format(*self._colors[:3])
        return "#" + ("{:02x}" * 4).format(*self._colors)

    def __eq__(self, other):
        try:
            other = shortcuts.check_color(other)
        except ValueError:
            return False
        else:
            return tuple(other) == tuple(self._color)

    colors = {}


def initialise_colors():
    for name, values in pygame.colordict.THECOLORS.items():
        c = color(values)
        color.colors[name] = c
    color.colors["transparent"] = color(0, 0, 0, 0)
