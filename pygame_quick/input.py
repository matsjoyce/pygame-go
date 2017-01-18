import pygame

from .shortcuts import with_pygame_inited, check_position


@with_pygame_inited
def mouse_position():
    return pygame.mouse.get_pos()


@with_pygame_inited
def set_mouse_position(x, y=None):
    pygame.mouse.set_pos(check_position(x, y))
