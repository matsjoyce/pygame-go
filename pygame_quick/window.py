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

import pygame

from . import image, events
from .shortcuts import with_pygame_inited, extract_size_args


class window(image.image):
    @with_pygame_inited
    def __init__(self, *args, frame_rate=20, autoquit=True, title="pygame-quick", icon=None, **kwargs):
        size = extract_size_args(args, kwargs)
        if pygame.display.get_surface():
            raise RuntimeError("You can only create one window!")
        self.icon = icon
        self._image = pygame.display.set_mode(size)
        self.frame_rate = frame_rate
        self._clock = pygame.time.Clock()
        self._active = True
        self._events = []
        self._autoquit = autoquit
        self.frame_number = 0
        self.title = title

        self.fill("white")

    def active(self):
        return self._active

    def stop(self):
        self._active = False

    def update(self):
        pygame.display.flip()
        self._clock.tick(self.frame_rate)
        self.frame_number += 1
        self._preprocess_events()

    def loop_forever(self):
        while self.active():
            self.update()

    def _preprocess_events(self):
        for event in pygame.event.get():
            type, info = events.expand_event(event)
            if type == events.EventType.quit and self._autoquit:
                self.stop()
            elif type is None:
                continue
            else:
                self._events.append((type, info))

    def has_events(self):
        return bool(self._events)

    def next_event(self):
        if self._events:
            return self._events.pop(0)
        raise ValueError("There are no more events")

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
    def title(self):
        return pygame.display.get_caption()

    @title.setter
    def title(self, name):
        pygame.display.set_caption(name)

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, image):
        self._icon = image
        if image is not None:
            pygame.display.set_caption(image)
