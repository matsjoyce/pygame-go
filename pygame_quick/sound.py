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
        self._channel = None
        self._paused = False

    def play(self, times=1, forever=False):
        self.stop()
        self._channel = pygame.mixer.find_channel()
        if self._channel is None:
            raise RuntimeError("No free channels! Try playing less sounds at once.")
        if forever:
            self._channel.play(self._sound, -1)
        else:
            self._channel.play(self._sound, times - 1)

    def stop(self):
        self._sound.stop()
        self._paused = False

    def pause(self):
        if self.is_playing():
            self._channel.pause()
            self._paused = True

    def unpause(self):
        if self.is_playing():
            self._channel.unpause()
            self._paused = False

    def is_playing(self):
        return self._channel is not None and self._channel.get_sound() == self._sound

    def is_paused(self):
        return self._paused

    @property
    def length(self):
        return self._sound.get_length()

    @property
    def volume(self):
        return self._sound.get_volume()

    @volume.setter
    def volume(self, value):
        self._sound.set_volume(value)
