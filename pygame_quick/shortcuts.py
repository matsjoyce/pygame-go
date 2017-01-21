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

from . import color, image


def with_pygame_inited(func=None):
    if func is None:
        # safe to call multiple times, noop if already called
        pygame.init()
        return

    @functools.wraps(func)
    def wpi_wrapper(*args, **kwargs):
        with_pygame_inited()
        return func(*args, **kwargs)
    return wpi_wrapper


def with_display_inited(func=None):
    if func is None:
        with_pygame_inited()
        if pygame.display.get_surface() is None:
            raise RuntimeError("Please create a window before calling this function")
        return

    @functools.wraps(func)
    def wdi_wrapper(*args, **kwargs):
        with_display_inited()
        return func(*args, **kwargs)
    return wdi_wrapper


def multi_format(multi_names):
    if len(multi_names) == 1:
        return multi_names[0]
    return ", ".join(multi_names[:-1]) + " and {}".format(multi_names[-1])


class ArgumentExtractor:
    def __init__(self, kwargs):
        self.kwargs = kwargs
        self.groups = set()

    def extract(self, single_name, multi_names, checker, optional=(), args=(), default=None, checker_args=()):
        self.groups.add((single_name, multi_names, optional))
        if args:
            return checker(args[0] if len(args) == 1 else args, *checker_args)
        try:
            return checker(self.kwargs.pop(single_name), *checker_args)
        except KeyError:
            pass
        try:
            return checker([self.kwargs.pop(i) for i in multi_names]
                           + [self.kwargs.pop(i) for i in optional if i in self.kwargs],
                           *checker_args)
        except KeyError:
            pass
        if default is not None:
            return default
        raise TypeError("You must give either {} or {}".format(single_name, multi_format(multi_names)))

    def extract_position(self, single_name="position", multi_names=("x", "y"), **kwargs):
        return self.extract(single_name, multi_names, check_position, **kwargs)

    def extract_size(self, single_name="size", multi_names=("width", "height"), **kwargs):
        return self.extract(single_name, multi_names, check_position, **kwargs)

    def extract_color(self, single_name="color", multi_names=("r", "g", "b"), optional=("a",), **kwargs):
        return self.extract(single_name, multi_names, check_color, optional, **kwargs)

    def extract_align(self, single_name="align", multi_names=("align_x", "align_y"), **kwargs):
        kwargs.setdefault("default", (0, 0))
        return self.extract(single_name, multi_names, check_align, **kwargs)

    def finalize(self):
        if not self.kwargs:
            return
        for name, value in self.kwargs.items():
            for single, multi, optional in self.groups:
                if name == single or name in multi or name in optional:
                    raise TypeError("You must give either {} or {}, not both!".format(single, multi_format(multi)))
            raise TypeError("Unknown argument '{}'".format(name))


def check_position(value):
    try:
        coord = [int(v) for v in value]
    except (TypeError, ValueError):
        try:
            value = iter(value)
        except (TypeError, ValueError):
            raise ValueError("Position must be iterable, not {}".format(type(value)))
        for v in value:
            try:
                int(v)
            except (TypeError, ValueError):
                raise ValueError("Position component must be a number, not {}".format(type(v)))
    if len(coord) == 2:
        return coord
    raise ValueError("Positions must have two components, not {}".format(len(coord)))


def check_color(value):
    if isinstance(value, color.color):
        return value.color
    elif isinstance(value, str):
        if value in color.color.colors:
            return color.color.colors[value].color
        else:
            raise ValueError("Unknown color '{}', maybe you spelt the name wrong?".format(value))
    try:
        value = iter(value)
    except (TypeError, ValueError):
        raise ValueError("Color must be iterable, not {}".format(type(value)))
    proc = []
    for v in value:
        try:
            proc.append(int(v) % 256)
        except (TypeError, ValueError):
            raise ValueError("Color component must be a number, not {}".format(type(v)))
    if len(proc) not in (3, 4):
        raise ValueError("Colors must have 3 or 4 components for RGBA")
    return tuple(proc)


def check_align(align, width, height):
    if align is image.Alignment.center:
        return width // 2, height // 2
    elif align is image.Alignment.topleft:
        return 0, 0
    elif align is image.Alignment.topright:
        return width, 0
    elif align is image.Alignment.bottomleft:
        return 0, height
    elif align is image.Alignment.bottomright:
        return width, height
    else:
        return check_position(align)
