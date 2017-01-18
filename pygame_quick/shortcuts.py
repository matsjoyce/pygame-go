import functools
import pygame


def with_pygame_inited(func):
    @functools.wraps(func)
    def wpi_wrapper(*args, **kwargs):
        # safe to call multiple times, noop if already called
        pygame.init()
        return func(*args, **kwargs)
    return wpi_wrapper
