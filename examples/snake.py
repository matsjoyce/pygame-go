import pygame_quick as pgq
import random

SNAKE_SIZE = 20

window = pgq.window(600, 400, framerate=5)

cx, cy = window.center
snake_dx, snake_dy = 0, SNAKE_SIZE
snake_dead = False
snake_parts = [(cx, cy - SNAKE_SIZE * i) for i in range(3)]
food_location = (random.randrange(window.width // SNAKE_SIZE) * SNAKE_SIZE,
                 random.randrange(window.height // SNAKE_SIZE) * SNAKE_SIZE)

head_image = pgq.image(SNAKE_SIZE, SNAKE_SIZE)
head_image.fill("white")
head_image.draw_circle(position=head_image.center, radius=2, color="black")
head_image.draw_hollow_rect(position=head_image.topleft, size=head_image.size, color="black")

tail_image_even = pgq.image(SNAKE_SIZE, SNAKE_SIZE)
tail_image_even.fill("yellow")

tail_image_odd = pgq.image(SNAKE_SIZE, SNAKE_SIZE)
tail_image_odd.fill("green")

food_image = pgq.image(SNAKE_SIZE, SNAKE_SIZE)
food_image.fill("red")

while window.active():
    window.fill("white")
    if snake_dead:
        window.draw_text(text="YOU DIED!", position=window.topleft, color="red", size=60)
        window.update()
        continue

    for _, key in window.events(pgq.key_down):
        if key == "<Left>" and snake_dx != SNAKE_SIZE:
            snake_dx, snake_dy = -SNAKE_SIZE, 0
        elif key == "<Right>" and snake_dx != -SNAKE_SIZE:
            snake_dx, snake_dy = SNAKE_SIZE, 0
        elif key == "<Up>" and snake_dy != SNAKE_SIZE:
            snake_dx, snake_dy = 0, -SNAKE_SIZE
        elif key == "<Down>" and snake_dy != -SNAKE_SIZE:
            snake_dx, snake_dy = 0, SNAKE_SIZE

    head_x, head_y = snake_parts[0]
    head_x = (head_x + snake_dx) % window.width
    head_y = (head_y + snake_dy) % window.height
    new_snake = [(head_x, head_y)] + snake_parts[:-1]
    if food_location in new_snake:
        new_snake.append(snake_parts[-1])
        food_location = (random.randrange(window.width // SNAKE_SIZE) * SNAKE_SIZE,
                         random.randrange(window.height // SNAKE_SIZE) * SNAKE_SIZE)
    snake_parts = new_snake
    snake_dead = snake_parts[0] in snake_parts[1:]

    for i, part in enumerate(snake_parts):
        if i == 0:
            head_image.draw(window, part)
        elif i % 2:
            tail_image_odd.draw(window, part)
        else:
            tail_image_even.draw(window, part)
    food_image.draw(window, food_location)
    window.update()
