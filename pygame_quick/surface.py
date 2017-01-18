import pathlib
import pygame

from .shortcuts import with_pygame_inited


class Surface:
    @with_pygame_inited
    def __init__(self, width, height):
        self._surf = pygame.Surface((width, height), pygame.SRCALPHA)

    @classmethod
    @with_pygame_inited
    def fromraw(cls, rawsurf):
        obj = cls.__new__(cls)
        obj._surf = rawsurf.convert_alpha()

    @classmethod
    def fromimage(cls, fname):
        path = pathlib.Path(fname).resolve()
        if not path.exists():
            raise FileNotFoundError("The file '{}' does not exist, maybe you spelt the name wrong?".format(path))
        try:
            return cls(pygame.image.load(str(path)))
        except pygame.error:
            raise IOError("Could not load '{}, are you sure its an image?".format(path))
