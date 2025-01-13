import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Step 3: Draw the game onto the screen
        screen.fill((0, 0, 0))  # Fill the screen with black

        pygame.display.flip()  # Update the full display Surface to the screen

    pygame.quit()

if __name__ == "__main__":
    main()