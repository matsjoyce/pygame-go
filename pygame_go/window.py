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

import pygame
import functools

from . import images, events
from .shortcuts import with_pygame_inited, ArgumentExtractor


def require_active(func):
    @functools.wraps(func)
    def ra_wrapper(self, *args, **kwargs):
        if not self.active():
            raise RuntimeError("Cannot call {} on a non-active window".format(func.__name__))
        return func(self, *args, **kwargs)
    return ra_wrapper


class window(images.image):
    @with_pygame_inited
    def __init__(self, *args, frame_rate=20, autoquit=True, title="pygame-go", icon=None, **kwargs):
        ae = ArgumentExtractor(kwargs)
        size = ae.extract_size(args=args)
        fill_with = ae.extract_color(default="white")
        ae.finalize()

        if pygame.display.get_surface():
            raise RuntimeError("You can only create one window!")
        self._active = True
        self.icon = icon
        self._image = pygame.display.set_mode(size)
        self.frame_rate = frame_rate
        self._clock = pygame.time.Clock()
        self._events = []
        self._autoquit = autoquit
        self.frame_number = 0
        self.title = title

        if fill_with is not None:
            self.fill(fill_with)

    def active(self):
        return self._active

    @require_active
    def stop(self):
        self._active = False
        pygame.quit()

    @require_active
    def update(self):
        pygame.display.flip()
        self._clock.tick(self.frame_rate)
        self.frame_number += 1
        self._preprocess_events()

    @require_active
    def loop_forever(self):
        while self.active():
            self.update()

    def _preprocess_events(self):
        for event in pygame.event.get():
            event = events.expand_event(event)
            if event is None:
                continue
            elif event.is_quit() and self._autoquit:
                self.stop()
            else:
                self._events.append(event)

    @require_active
    def has_events(self):
        return bool(self._events)

    @require_active
    def next_event(self):
        if self._events:
            return self._events.pop(0)
        raise ValueError("There are no more events")

    @require_active
    def events(self):
        while self.has_events():
            yield self.next_event()

    def flip(self, x=False, y=False):
        raise RuntimeError("Cannot flip a window")

    def rotate(self, angle):
        raise RuntimeError("Cannot rotate a window")

    def scale(self, times):
        raise RuntimeError("Cannot scale a window")

    @property
    @require_active
    def title(self):
        return pygame.display.get_caption()

    @title.setter
    @require_active
    def title(self, name):
        pygame.display.set_caption(name)

    @property
    @require_active
    def icon(self):
        return self._icon

    @icon.setter
    @require_active
    def icon(self, image):
        self._icon = image
        if image is not None:
            pygame.display.set_caption(image)
