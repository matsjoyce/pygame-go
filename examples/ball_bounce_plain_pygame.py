"""
ball_bounce_plain_pygame.py
========
Bounce a ball around the screen. Uses vanilla pygame. Compare this to ball_bounce.py

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
