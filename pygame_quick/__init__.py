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

from .window import window
from .image import image, Alignment
from .events import EventType, Button, ScrollDirection, ScrollDirection
from .input import mouse_position, set_mouse_position, is_key_pressed, is_mouse_pressed
from .color import color, initialise_colors
from .sound import sound

initialise_colors()
color_names = list(color.colors)


def extract_values(enum, suffix, scope):
    for value in enum:
        scope[value.name + suffix] = value


# provide shortcuts to the enum values
extract_values(EventType, "", locals())
extract_values(Button, "_button", locals())
extract_values(ScrollDirection, "_scroll", locals())
extract_values(Alignment, "", locals())

# Leave module level as clean as possible

del extract_values, initialise_colors
del EventType, Button, ScrollDirection, Alignment
