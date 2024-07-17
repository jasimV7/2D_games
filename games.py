import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # Adjust the resolution as needed
pygame.display.set_caption("My Pygame Window")

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Update game state

    # Draw graphics
    screen.fill((255, 255, 255))  # Fill the screen with white

    # Flip the display
    pygame.display.flip()

# End of game loop
