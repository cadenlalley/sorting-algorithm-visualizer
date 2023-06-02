import pygame
import random

pygame.init()

WIDTH = 1280
HEIGHT = 720
NUM_BARS = 360 
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BAR_WIDTH = WIDTH / NUM_BARS

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Caden Lalley - Algorithm Visualizer")

bar_creation_height = HEIGHT
bars_list = [None] * (NUM_BARS)
for i in range(0, NUM_BARS):
    bars_list[i] = bar_creation_height
    bar_creation_height = bar_creation_height - HEIGHT * (1 / NUM_BARS)

random.shuffle(bars_list)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))


    previous_bar_x = 0
    for current_bar_height in bars_list:
        rectangle = pygame.Rect(previous_bar_x, (HEIGHT - current_bar_height), int(BAR_WIDTH), current_bar_height)
        pygame.draw.rect(screen, WHITE, rectangle)     
        previous_bar_x += BAR_WIDTH 

    pygame.display.flip()

pygame.quit()
