import pathlib
import pygame

from . import color
from .shortcuts import with_pygame_inited, check_position, check_color


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

    def fill(self, r, g=None, b=None, a=None):
        self._surf.fill(check_color(r, g, b, a))

    def copy(self):
        return self.fromraw(self._surf.copy())

    @property
    def size(self):
        return self._surf.get_size()

    @property
    def width(self):
        return self._surf.get_width()

    @property
    def height(self):
        return self._surf.get_height()

    @property
    def center(self):
        w, h = self._surf.get_size()
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
    def topleft(self):
        return self.size

    def draw(self, onto_surf, x, y=None):
        onto_surf._surf.blit(self._surf, check_position(x, y))

    def draw_by_center(self, onto_surf, x, y=None):
        x, y = check_position(x, y)
        w, h = self.size
        x -= w // 2
        y -= h // 2
        onto_surf._surf.blit(self._surf, (x, y))
