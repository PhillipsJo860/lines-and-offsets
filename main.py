# Joshua Phillips
# date
# Pygame Template(project)

# Import the pygame and system modules
import pygame
import sys
import config

# --- Constants --- #

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 60 

WHITE = (255, 255, 255) # RGB triplet saved in a tuple


#  --- Initialize Pygame --- #
pygame.init()

#  --- Screen setup --- #
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pygame Template')

# --- Clock setup --- #
clock = pygame.time.Clock() #The capital C in CLock is important

# --- Game loop --- #
running = True
while running:
    # --- liston for and handle events --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Uppercase for quit is also important
            running = False


    # --- Game Logic --- #
    # --- Draw --- #
    screen.fill(WHITE)
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, config.COLOR_GOLDENROD, [800, 10 + y_offset], [0, 600 + y_offset], 5)
    x_offset = 0
    while x_offset < 130:
        pygame.draw.line(screen, config.COLOR_PALEVIOLETRED, [-130 + x_offset, 14], [800 + x_offset, 600], 5)
        x_offset = x_offset + 14
    # This is where you draw game objects:

    pygame.display.flip() # updateing the display

    # limit FPS
    clock.tick(FPS)



pygame.quit()
sys.exit()