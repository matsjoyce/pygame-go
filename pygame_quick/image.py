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

import enum
import pathlib
import pygame
import os

from . import color, rendertext
from .shortcuts import with_pygame_inited, with_display_inited
from .shortcuts import extract_position_args, extract_position_kwargs
from .shortcuts import extract_size_args, extract_size_kwargs
from .shortcuts import extract_color_args, extract_color_kwargs
from .shortcuts import check_position, extract_align_kwargs


class Alignment(enum.Enum):
    center = "center"
    topleft = "topleft"
    topright = "topright"
    bottomleft = "bottomleft"
    bottomright = "bottomright"


class image:
    @with_pygame_inited
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], (str, pathlib.Path)) or "fname" in kwargs:
            fname = str(args[0] if args else kwargs["fname"])
            path = pathlib.Path(os.path.expanduser(fname)).resolve()
            if not path.exists():
                raise FileNotFoundError("The file '{}' does not exist, maybe you spelt the name wrong?".format(path))
            with_display_inited()
            try:
                self._image = pygame.image.load(str(path)).convert_alpha()
            except pygame.error:
                raise IOError("Could not load '{}', are you sure it's an image?".format(path))

        else:
            if "color" in kwargs or "r" in kwargs:
                fill_with = extract_color_kwargs(kwargs)
            else:
                fill_with = None
            size = extract_size_args(args, kwargs)
            self._image = pygame.Surface(size, pygame.SRCALPHA)
            if fill_with is not None:
                self.fill(fill_with)

    @classmethod
    @with_display_inited
    def fromraw(cls, rawimage):
        obj = cls.__new__(cls)
        obj._image = rawimage.convert_alpha()
        return obj

    def fill(self, *args, **kwargs):
        self._image.fill(extract_color_args(args, kwargs))

    def copy(self):
        return self.fromraw(self._image.copy())

    @property
    def size(self):
        return self._image.get_size()

    @property
    def width(self):
        return self._image.get_width()

    @property
    def height(self):
        return self._image.get_height()

    @property
    def center(self):
        w, h = self._image.get_size()
        return w // 2, h // 2

    @property
    def topleft(self):
        return 0, 0

    @property
    def topright(self):
        return self.width, 0

    @property
    def bottomleft(self):
        return 0, self.height

    @property
    def bottomright(self):
        return self.size

    def draw_image(self, image, *args, **kwargs):
        ox, oy = extract_align_kwargs(kwargs, image._image.get_size())
        x, y = extract_position_args(args, kwargs)

        self._image.blit(image._image, (x - ox, y - oy))

    def draw_rect(self, **kwargs):
        x, y = extract_position_kwargs(kwargs)
        width, height = extract_size_kwargs(kwargs)
        color = extract_color_kwargs(kwargs)
        ox, oy = extract_align_kwargs(kwargs, (width, height))
        pygame.draw.rect(self._image, color, (x - ox, y - oy, width, height))

    def draw_hollow_rect(self, *, thickness=1, **kwargs):
        # make consistent with draw_hollow_circle
        color = extract_color_kwargs(kwargs)
        x, y = extract_position_kwargs(kwargs)
        width, height = extract_size_kwargs(kwargs)
        ox, oy = extract_align_kwargs(kwargs, (width, height))
        x -= ox
        y -= oy
        pygame.draw.rect(self._image, color, (x, y, thickness, height))
        pygame.draw.rect(self._image, color, (x + width - thickness, y, thickness, height))
        if thickness > 1:
            pygame.draw.rect(self._image, color, (x, y, width, thickness))
            pygame.draw.rect(self._image, color, (x, y + height - thickness, width, thickness))
        else:
            pygame.draw.line(self._image, color, (x, y), (x + width - 1, y))
            pygame.draw.line(self._image, color, (x, y + height - 1), (x + width - 1, y + height - 1))

    def draw_circle(self, *, radius, **kwargs):
        position = extract_position_kwargs(kwargs)
        color = extract_color_kwargs(kwargs)
        pygame.draw.circle(self._image, color, position, radius)

    def draw_hollow_circle(self, *, radius, thickness=1, **kwargs):
        position = extract_position_kwargs(kwargs)
        color = extract_color_kwargs(kwargs)
        pygame.draw.circle(self._image, color, position, radius, thickness)

    def draw_line(self, *, thickness=1, **kwargs):
        color = extract_color_kwargs(kwargs)
        start = extract_position_kwargs(kwargs, "start", ("start_x", "start_y"))
        end = extract_position_kwargs(kwargs, "end", ("end_x", "end_y"))
        pygame.draw.line(self._image, color, start, end, thickness)

    def draw_text(self, *, text, size=30, font=None, bold=False, italic=False, **kwargs):
        if "\n" in text:
            raise TypeError("Cannot render newlines")

        color = extract_color_kwargs(kwargs)
        font = rendertext.get_font(size, font, bold, italic)
        textimage = font.render(text, True, color)
        ox, oy = extract_align_kwargs(kwargs, textimage.get_size())
        x, y = extract_position_kwargs(kwargs)

        self._image.blit(textimage, (x - ox, y - oy))

    def flip(self, vertical=False, horizontal=False):
        self._image = pygame.transform.flip(self._image, horizontal, vertical)

    def rotate(self, angle):
        self._image = pygame.transform.rotate(self._image, -(angle % 360))

    def scale(self, times):
        self._image = pygame.transform.smoothscale(self._image, (self.width * times, self.height * times))
