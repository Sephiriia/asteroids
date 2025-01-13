import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Step 3: Draw the game onto the screen
        screen.fill((0, 0, 0))  # Fill the screen with black

        player.draw(screen)

        pygame.display.flip()  # Update the full display Surface to the screen

        dt = clock.tick(60) / 1000


    pygame.quit()

if __name__ == "__main__":
    main()