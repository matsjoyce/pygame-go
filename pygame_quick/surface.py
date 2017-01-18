import pathlib
import pygame

from . import color, rendertext
from .shortcuts import with_pygame_inited
from .shortcuts import extract_position_args, extract_position_kwargs
from .shortcuts import extract_size_args, extract_size_kwargs
from .shortcuts import extract_color_args, extract_color_kwargs


class surface:
    @with_pygame_inited
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], (str, pathlib.Path)) or "fname" in kwargs:
            path = pathlib.Path(args[0] if args else kwargs["fname"]).resolve()
            if not path.exists():
                raise FileNotFoundError("The file '{}' does not exist, maybe you spelt the name wrong?".format(path))
            try:
                self._surf = pygame.image.load(str(path))
            except pygame.error:
                raise IOError("Could not load '{}, are you sure its an image?".format(path))

        else:
            size = extract_size_args(args, kwargs)
            self._surf = pygame.Surface(size, pygame.SRCALPHA)

    @classmethod
    @with_pygame_inited
    def fromraw(cls, rawsurf):
        obj = cls.__new__(cls)
        obj._surf = rawsurf.convert_alpha()

    def fill(self, *args, **kwargs):
        self._surf.fill(extract_color_args(args, kwargs))

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
    def bottomright(self):
        return self.size

    def draw(self, onto_surf, *args, **kwargs):
        onto_surf._surf.blit(self._surf, extract_position_args(args, kwargs))

    draw_by_topleft = draw

    def draw_by_center(self, onto_surf, *args, **kwargs):
        x, y = extract_position_args(args, kwargs)
        w, h = self.size
        x -= w // 2
        y -= h // 2
        self.draw(onto_surf, x, y)

    def draw_by_topright(self, onto_surf, *args, **kwargs):
        x, y = extract_position_args(args, kwargs)
        w, h = self.size
        x -= w
        self.draw(onto_surf, x, y)

    def draw_by_bottomleft(self, onto_surf, *args, **kwargs):
        x, y = extract_position_args(args, kwargs)
        w, h = self.size
        y -= h
        self.draw(onto_surf, x, y)

    def draw_by_bottomright(self, onto_surf, *args, **kwargs):
        x, y = extract_position_args(args, kwargs)
        w, h = self.size
        x -= w
        y -= h
        self.draw(onto_surf, x, y)

    def draw_rectangle(self, **kwargs):
        position = extract_position_kwargs(kwargs)
        size = extract_size_kwargs(kwargs)
        color = extract_color_kwargs(kwargs)
        pygame.draw.rect(self._surf, color, position + size)

    def draw_hollow_rectangle(self, *, thickness=1, **kwargs):
        # make consistent with draw_hollow_circle
        x, y = extract_position_kwargs(kwargs)
        width, height = extract_size_kwargs(kwargs)
        color = extract_color_kwargs(kwargs)
        pygame.draw.rect(self._surf, color, (x, y, thickness, height))
        pygame.draw.rect(self._surf, color, (x, y, width, thickness))
        pygame.draw.rect(self._surf, color, (x + width - thickness, y, thickness, height))
        pygame.draw.rect(self._surf, color, (x, y + height - thickness, width, thickness))

    def draw_circle(self, *, radius, **kwargs):
        position = extract_position_kwargs(kwargs)
        color = extract_color_kwargs(kwargs)
        pygame.draw.circle(self._surf, color, position, radius)

    def draw_hollow_circle(self, *, radius, thickness=1, **kwargs):
        position = extract_position_kwargs(kwargs)
        color = extract_color_kwargs(kwargs)
        pygame.draw.circle(self._surf, color, position, radius, thickness)

    def draw_line(self, *, thickness=1, **kwargs):
        color = extract_color_kwargs(kwargs)
        start = extract_position_kwargs(kwargs, "start", ("start_x", "start_y"))
        end = extract_position_kwargs(kwargs, "end", ("end_x", "end_y"))
        pygame.draw.line(self._surf, color, start, end, thickness)

    def draw_text(self, *, text, size=30, font=None, bold=False, italic=False, **kwargs):
        if "\n" in text:
            raise TypeError("Cannot render newlines")
        color = extract_color_kwargs(kwargs)
        position = extract_position_kwargs(kwargs)
        font = rendertext.get_font(size, font, bold, italic)
        textsurf = font.render(text, True, color)
        self._surf.blit(textsurf, position)
