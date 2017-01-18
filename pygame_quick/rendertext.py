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
