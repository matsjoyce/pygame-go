"""
pygame-go - PyGame for Humans!
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
from .images import image, Alignment
from .events import Button, ScrollDirection, ScrollDirection
from .input import mouse_position, set_mouse_position, is_key_pressed, is_mouse_pressed, monitor_size
from .colors import color, initialise_colors
from .sound import sound
from .collisions import collides_rect_rect, collides_circle_circle

__version__ = "0.1.0-alpha"
__author__ = "Matthew Joyce"
__author_email__ = "matsjoyce@gmail.com"
__copyright__ = "2017, Matthew Joyce"
__credits__ = ["Matthew Joyce"]
__license__ = "LGPLv3"
__maintainer__ = "Matthew Joyce"
__email__ = "matsjoyce@gmail.com"
__status__ = "Development"

__all__ = ["window", "image", "mouse_position", "set_mouse_position", "is_key_pressed",
           "is_mouse_pressed", "monitor_size", "color", "color_names", "sound"]

initialise_colors()
color_names = list(color.colors)


def extract_values(enum, suffix, scope):
    for value in enum:
        scope[value.name + suffix] = value
        __all__.append(value.name + suffix)


# provide shortcuts to the enum values
extract_values(Button, "_button", locals())
extract_values(ScrollDirection, "_scroll", locals())
extract_values(Alignment, "", locals())

# Leave module level as clean as possible

del extract_values, initialise_colors
del Button, ScrollDirection, Alignment
