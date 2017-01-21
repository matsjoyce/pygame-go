import pathlib
import pygame
import os

from .shortcuts import with_pygame_inited


class sound:
    @with_pygame_inited
    def __init__(self, fname):
        path = pathlib.Path(os.path.expanduser(fname)).resolve()
        if not path.exists():
            raise FileNotFoundError("The file '{}' does not exist, maybe you spelt the name wrong?".format(path))
        try:
            self._sound = pygame.mixer.Sound(str(path))
        except pygame.error:
            raise IOError("Could not load '{}', are you sure it's an sound file (.ogg or .wav)?".format(path))
        self._channels = []

    def is_playing(self):
        playing = False
        new_channels = []
        for channel in self._channels:
            if channel.get_sound() == self._sound:
                playing = True
                new_channels.append(channel)
        self._channels = new_channels
        return playing

    def play(self, times=1, forever=False):
        if forever:
            channel = self._sound.play(-1)
        else:
            channel = self._sound.play(times - 1)
        self._channels.append(channel)
        self.is_playing()

    def stop(self):
        self._sound.stop()
        self.is_playing()

    @property
    def volume(self):
        return self._sound.get_volume()

    @volume.setter
    def volume(self, value):
        self._sound.set_volume(value)

    @property
    def length(self):
        return self._sound.get_length()
