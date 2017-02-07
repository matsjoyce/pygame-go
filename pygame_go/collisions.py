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

from .shortcuts import ArgumentExtractor


def collides_rect_rect(**kwargs):
    # http://stackoverflow.com/q/2752349

    ae = ArgumentExtractor(kwargs)
    x_a, y_a = ae.extract_position("position_a", ("x_a", "y_a"))
    x_b, y_b = ae.extract_position("position_b", ("x_b", "y_b"))
    width_a, height_a = ae.extract_size("size_a", ("width_a", "height_a"))
    width_b, height_b = ae.extract_size("size_b", ("width_b", "height_b"))
    ox_a, oy_a = ae.extract_align("align_a", ("align_x_a", "align_y_a"), checker_args=(width_a, height_a))
    ox_b, oy_b = ae.extract_align("align_b", ("align_x_b", "align_y_b"), checker_args=(width_b, height_b))
    ae.finalize()

    x_a -= ox_a
    y_a -= oy_a
    x_b -= ox_b
    y_b -= oy_b

    return (x_b <= x_a + width_a
            and x_a <= x_b + width_b
            and y_b <= y_a + height_a
            and y_a <= y_b + height_b)
