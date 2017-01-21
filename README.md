pygame-quick
============

A simplified version of PyGame for use in teaching

[![Documentation Status](https://readthedocs.org/projects/pygame-quick/badge/?version=latest)](http://pygame-quick.readthedocs.io/en/latest/?badge=latest)

Example
-------

Bounce a red ball around the screen:

```py3
import pygame_quick as pgq

BALL_RADIUS = 50

window = pgq.window(800, 600, frame_rate=60)

ball_x, ball_y = window.center
ball_dx = ball_dy = 5
bounces = 0

while window.active():
    bounced = False
    if ball_x in (BALL_RADIUS, window.width - BALL_RADIUS):
        ball_dx = -ball_dx
        bounced = True
    if ball_y in (BALL_RADIUS, window.height - BALL_RADIUS):
        ball_dy = -ball_dy
        bounced = True

    bounces += bounced
    ball_x += ball_dx
    ball_y += ball_dy

    window.fill("white")
    window.draw_circle(x=ball_x, y=ball_y, color="red", radius=BALL_RADIUS)
    window.draw_text(text="{} bounces".format(bounces), position=window.topleft, color="black")
    window.update()
```

Equivalent pygame-only code:

```py3
import pygame

BG_COLOR = (255, 255, 255)
BALL_COLOR = (255, 0, 0)
TEXT_COLOR = (0, 0, 0)
BALL_RADIUS = 50
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

active = True

ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
ball_dx = ball_dy = 5
bounces = 0

clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 30)

while active:
    bounced = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    if ball_x in (BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS):
        ball_dx = -ball_dx
        bounced = True
    if ball_y in (BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS):
        ball_dy = -ball_dy
        bounced = True

    bounces += bounced
    ball_x += ball_dx
    ball_y += ball_dy

    screen.fill(BG_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
    surf = font.render("{} bounces".format(bounces), True, TEXT_COLOR)
    screen.blit(surf, (0, 0))

    pygame.display.flip()
    clock.tick(60)
```

Documentation
-------------

Go to https://pygame-quick.rtfd.io.

Requirements
------------

 - [PyGame](https://pypi.python.org/pypi/Pygame) (must be the python 3 version)

And either:

 - Python 3.4+

Or:

  - Python 3
  - [pathlib](https://pypi.python.org/pypi/pathlib)
  - [enum34](https://pypi.python.org/pypi/enum34)

Installation
------------

```bash
git clone https://github.com/matsjoyce/pygame-quick.git
cd pygame-quick
python3 setup.py install
```
