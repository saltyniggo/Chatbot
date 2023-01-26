import pygame
import time

# initialize pygame
pygame.init()

# set the window size
width = 500
height = 500

# set the snake's starting position and size
snake_x = 250
snake_y = 250
snake_size = 10

# set the initial speed of the snake
snake_speed = 20

# set the initial direction of the snake
snake_direction = "right"

# set the window
win = pygame.display.set_mode((width, height))

# set the title of the window
pygame.display.set_caption("Snake Game")

# create a game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # move the snake
    if snake_direction == "right":
        snake_x += snake_speed
    if snake_direction == "left":
        snake_x -= snake_speed
    if snake_direction == "up":
        snake_y -= snake_speed
    if snake_direction == "down":
        snake_y += snake_speed

    # check for collision with the walls
    if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
        pygame.quit()
        quit()

    # update the window
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (snake_x, snake_y, snake_size, snake_size))
    pygame.display.update()
    time.sleep(0.05)
