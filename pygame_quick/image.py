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
import functools
import pathlib
import pygame
import os

from . import color as color_mod
from .shortcuts import with_pygame_inited, with_display_inited, ArgumentExtractor


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
            ae = ArgumentExtractor(kwargs)
            size = ae.extract_size(args=args)
            fill_with = ae.extract_color(default="")
            ae.finalize()

            self._image = pygame.Surface(size, pygame.SRCALPHA)
            if fill_with != "":
                self.fill(fill_with)

    @classmethod
    @with_display_inited
    def fromraw(cls, rawimage):
        obj = cls.__new__(cls)
        obj._image = rawimage.convert_alpha()
        return obj

    def fill(self, *args, **kwargs):
        ae = ArgumentExtractor(kwargs)
        color = ae.extract_color(args=args)
        ae.finalize()
        self._image.fill(color)

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
        ae = ArgumentExtractor(kwargs)
        x, y = ae.extract_position(args=args)
        ox, oy = ae.extract_align(checker_args=image._image.get_size())
        ae.finalize()

        self._image.blit(image._image, (x - ox, y - oy))

    def draw_rect(self, **kwargs):
        ae = ArgumentExtractor(kwargs)
        x, y = ae.extract_position()
        width, height = ae.extract_size()
        color = ae.extract_color()
        ox, oy = ae.extract_align(checker_args=(width, height))
        ae.finalize()

        pygame.draw.rect(self._image, color, (x - ox, y - oy, width, height))

    def draw_hollow_rect(self, *, thickness=1, **kwargs):
        # make consistent with draw_hollow_circle
        ae = ArgumentExtractor(kwargs)
        x, y = ae.extract_position()
        width, height = ae.extract_size()
        color = ae.extract_color()
        ox, oy = ae.extract_align(checker_args=(width, height))
        ae.finalize()

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
        ae = ArgumentExtractor(kwargs)
        position = ae.extract_position()
        color = ae.extract_color()
        ae.finalize()

        pygame.draw.circle(self._image, color, position, radius)

    def draw_hollow_circle(self, *, radius, thickness=1, **kwargs):
        ae = ArgumentExtractor(kwargs)
        position = ae.extract_position()
        color = ae.extract_color()
        ae.finalize()

        pygame.draw.circle(self._image, color, position, radius, thickness)

    def draw_ellipse(self, **kwargs):
        ae = ArgumentExtractor(kwargs)
        width, height = ae.extract_size()
        x, y = ae.extract_position()
        color = ae.extract_color()
        ae.finalize()

        x -= width // 2
        y -= height // 2

        pygame.draw.ellipse(self._image, color, (x, y, width, height))

    def draw_hollow_ellipse(self, *, thickness=1, **kwargs):
        ae = ArgumentExtractor(kwargs)
        width, height = ae.extract_size()
        x, y = ae.extract_position()
        color = ae.extract_color()
        ae.finalize()

        x -= width // 2
        y -= height // 2

        pygame.draw.ellipse(self._image, color, (x, y, width, height), thickness)

    def draw_line(self, *, thickness=1, **kwargs):
        ae = ArgumentExtractor(kwargs)
        start = ae.extract_position("start", ("start_x", "start_y"))
        end = ae.extract_position("end", ("end_x", "end_y"))
        color = ae.extract_color()
        ae.finalize()

        pygame.draw.line(self._image, color, start, end, thickness)

    @staticmethod
    @with_pygame_inited
    @functools.lru_cache(None)
    def _all_fonts():
        return pygame.font.get_fonts()

    def draw_text(self, *, text, size=30, font=None, bold=False, italic=False, **kwargs):
        if "\n" in text:
            raise TypeError("Cannot render newlines")

        if font is None:
            fname = pygame.font.get_default_font()
        elif font not in self._all_fonts():
            raise ValueError("Unknown font, choose from {}".format(", ".join(self._all_fonts())))
        else:
            fname = pygame.font.match_font(font, bold, italic)
        font = pygame.font.Font(fname, size)

        ae = ArgumentExtractor(kwargs)
        color = ae.extract_color()
        textimage = font.render(text, True, color)
        ox, oy = ae.extract_align(checker_args=textimage.get_size())
        x, y = ae.extract_position()
        ae.finalize()

        self._image.blit(textimage, (x - ox, y - oy))

    def flip(self, vertical=False, horizontal=False):
        self._image = pygame.transform.flip(self._image, horizontal, vertical)

    def rotate(self, angle):
        self._image = pygame.transform.rotate(self._image, -(angle % 360))

    def scale(self, times):
        self._image = pygame.transform.smoothscale(self._image, (self.width * times, self.height * times))

    def color_at(self, *args, **kwargs):
        ae = ArgumentExtractor(kwargs)
        x, y = ae.extract_position(args=args)
        ae.finalize()

        return color_mod.color(self._image.get_at((x, y)))
