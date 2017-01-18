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


def check_position(x, y):
    if isinstance(x, tuple):
        check = x
    else:
        check = x, y
    return tuple(map(int, check))


def check_color(r, g, b, a):
    if isinstance(r, color.Color):
        return r.color
    elif isinstance(r, tuple):
        check = r
    elif isinstance(r, str):
        check = color.all_colors[r].color
    else:
        if a is None:
            check = r, g, b
        else:
            check = r, g, b, a
    if len(check) not in (3, 4):
        raise ValueError("Colors must have 3 or 4 components for RGBA")
    print(tuple(map(color.put_in_range, check)))
    return tuple(map(color.put_in_range, check))
