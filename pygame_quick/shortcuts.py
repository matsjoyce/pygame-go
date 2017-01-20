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
import collections

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


def extract_position_kwargs(kwargs, single_name="position", multi_names=("x", "y")):
    got_in_single = single_name in kwargs
    got_in_multi = all(i in kwargs for i in multi_names)
    if got_in_single and got_in_multi:
        raise TypeError("You must give either {} or {}, {} and {}, not both!".format(single_name, *multi_names[:3]))
    elif got_in_single:
        pos = kwargs[single_name]
    elif got_in_multi:
        pos = (kwargs[i] for i in multi_names)
    else:
        raise TypeError("You must give either {} or {} and {}".format(single_name, *multi_names))
    return check_position(pos)


def extract_position_args(args, kwargs, *kwarg_extract):
    if not args:
        return extract_position_kwargs(kwargs, *kwarg_extract)
    elif len(args) > 1:
        color = args
    else:
        color = args[0]
    if kwargs:
        raise TypeError("Unused arguments {}. Either use position arguments or keyword arguments, not both!".format(kwargs))
    return check_position(color)


def check_position(value):
    if not isinstance(value, collections.abc.Iterable):
        raise ValueError("Color must be iterable, not {}".format(type(value)))
    value = tuple(value)
    if len(value) != 2:
        raise ValueError("Positions must have two components")
    for v in value:
        if not isinstance(v, (int, float)):
            raise RuntimeError("Position component must be a number, not {}".format(type(v)))
    return tuple(map(int, value))


def extract_size_kwargs(kwargs, single_name="size", multi_names=("width", "height")):
    return extract_position_kwargs(kwargs, single_name, multi_names)


def extract_size_args(args, kwargs, single_name="size", multi_names=("width", "height")):
    return extract_position_args(args, kwargs, single_name, multi_names)


def color_clamp(value):
    return int(value) % 256


def extract_color_kwargs(kwargs, single_name="color", multi_names=("r", "g", "b", "a")):
    got_in_single = single_name in kwargs
    got_in_multi = all(i in kwargs for i in multi_names[:3])
    if got_in_single and got_in_multi:
        raise TypeError("You must give either {} or {}, {} and {}, not both!".format(single_name, *multi_names[:3]))
    elif got_in_single:
        color = kwargs[single_name]
    elif got_in_multi:
        r, g, b = (kwargs[i] for i in multi_names[:3])
        a = kwargs.get(multi_names[-1], 255)
        color = r, g, b, a
    else:
        raise TypeError("You must give either {} or {}, {} and {}".format(single_name, *multi_names[:3]))
    return check_color(color)


def extract_color_args(args, kwargs, *kwarg_extract):
    if not args:
        return extract_color_kwargs(kwargs, *kwarg_extract)
    elif len(args) > 1:
        color = args
    else:
        color = args[0]
    if kwargs:
        raise TypeError("Unused arguments {}. Either use position arguments or keyword arguments, not both!".format(kwargs))
    return check_color(color)


def check_color(value):
    if isinstance(value, color.color):
        return value.color
    elif isinstance(value, str):
        if value in color.color.colors:
            return color.color.colors[value].color
        else:
            raise ValueError("Unknown color '{}', maybe you spelt the name wrong?".format(value))
    elif not isinstance(value, collections.abc.Iterable):
        raise ValueError("Color must be iterable, not {}".format(type(value)))
    value = tuple(value)
    if len(value) not in (3, 4):
        raise ValueError("Colors must have 3 or 4 components for RGBA")
    for v in value:
        if not isinstance(v, (int, float)):
            raise RuntimeError("Color component must be a number, not {}".format(type(v)))
    return tuple(map(color.color_clamp, value))


def translate_align(align, width, height):
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


def extract_align_kwargs(kwargs, size, single_name="align", multi_names=("align_x", "align_y")):
    if "align" in kwargs:
        if "align_x" in kwargs:
            raise TypeError("You can only give align or align_x and align_y, not both!")
        if kwargs["align"] in image.Alignment:
            return translate_align(kwargs.pop("align"), *size)
        else:
            return check_position(kwargs.pop("align"))
    elif "align_x" in kwargs or "align_y" in kwargs:
        if "align_x" in kwargs and "align_y" in kwargs:
            return check_position((kwargs.pop("align_x"), kwargs.pop("align_y")))
        else:
            raise TypeError("You must give both align_x and align_y, or neither!")
    else:
        return 0, 0
