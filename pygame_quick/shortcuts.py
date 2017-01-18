import functools
import pygame

from . import color


def with_pygame_inited(func):
    @functools.wraps(func)
    def wpi_wrapper(*args, **kwargs):
        # safe to call multiple times, noop if already called
        pygame.init()
        return func(*args, **kwargs)
    return wpi_wrapper


def extract_position_kwargs(kwargs, single_name="position", multi_names=("x", "y")):
    if single_name in kwargs:
        pos = kwargs[single_name]
    elif all(i in kwargs for i in multi_names):
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
        raise TypeError("Unused keyword arguments {}".format(kwargs))
    return check_position(color)


def check_position(value):
    return tuple(map(int, value))


def extract_size_kwargs(kwargs, single_name="size", multi_names=("width", "height")):
    return extract_position_kwargs(kwargs, single_name, multi_names)


def extract_size_args(args, kwargs, single_name="size", multi_names=("width", "height")):
    return extract_position_args(args, kwargs, single_name, multi_names)


def color_clamp(value):
    return int(value) % 256


def extract_color_kwargs(kwargs, single_name="color", multi_names=("r", "g", "b", "a")):
    if single_name in kwargs:
        color = kwargs[single_name]
    elif all(i in kwargs for i in multi_names[:3]):
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
        raise TypeError("Unused keyword arguments {}".format(kwargs))
    return check_color(color)


def check_color(value):
    if isinstance(value, color.color):
        return value.color
    elif isinstance(value, str):
        return color.color.colors[value].color
    value = tuple(value)
    if len(value) not in (3, 4):
        raise ValueError("Colors must have 3 or 4 components for RGBA")
    return tuple(map(color.color_clamp, value))
