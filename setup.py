#!/usr/bin/env python3

from distutils.core import setup
import sys
import pygame_go as pygo

setup(name="pygame-go",
      version=pygo.__version__,
      author=pygo.__author__,
      author_email=pygo.__author_email__,
      maintainer=pygo.__maintainer__,
      maintainer_email=pygo.__email__,
      description="A simplified version of pygame for use in teaching",
      url="https://github.com/matsjoyce/pygame-go",
      download_url="https://github.com/matsjoyce/pygame-go/releases",
      packages=["pygame_go"],
      classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: X11 Applications",
            "Intended Audience :: Education",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.0",
            "Programming Language :: Python :: 3.1",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Education",
            "Topic :: Games/Entertainment",
            "Topic :: Multimedia :: Graphics"
            "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
            ]
      )
