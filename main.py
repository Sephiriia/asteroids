import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        # Update the player
        player.update(dt)

        # Step 3: Draw the game onto the screen
        screen.fill((0, 0, 0))  # Fill the screen with black

        player.draw(screen)

        pygame.display.flip()  # Update the full display Surface to the screen

    pygame.quit()

if __name__ == "__main__":
    main()