import pygame

from .shortcuts import color_clamp, extract_color_args


class color:
    def __init__(self, *args, **kwargs):
        self._color = extract_color_args(args, kwargs)

    @classmethod
    def fromhex(cls, value):
        if value.startswith("#"):
            value = value[1:]
        if len(value) in (3, 4):
            value = "".join(i + i for i in value)
        if len(value) not in (6, 8):
            raise ValueError("The color is the wrong length")
        chunks = [value[i * 2:(i + 1) * 2] for i in range(len(value) // 2)]
        try:
            chunks = [int(i, 16) for i in chunks]
        except:
            raise ValueError("The color must be in hexadecimal")
        return cls(*chunks)

    @property
    def r(self):
        return self._color[0]

    @r.setter
    def r(self, value):
        self._color[0] = color_clamp(value)

    @property
    def g(self):
        return self._color[1]

    @g.setter
    def g(self, value):
        self._color[1] = color_clamp(value)

    @property
    def b(self):
        return self._color[2]

    @b.setter
    def b(self, value):
        self._color[2] = color_clamp(value)

    @property
    def transparency(self):
        return self._color[3]

    @transparency.setter
    def transparency(self, value):
        self._color[3] = color_clamp(value)

    @property
    def color(self):
        return tuple(self._color)

    @property
    def hex(self):
        if self._colors[3] == 255:
            return "#" + ("{:02x}" * 3).format(*self._colors[:3])
        return "#" + ("{:02x}" * 4).format(*self._colors)

    colors = {}

for name, values in pygame.colordict.THECOLORS.items():
    c = color(values)
    setattr(color, name, c)
    color.colors[name] = c
