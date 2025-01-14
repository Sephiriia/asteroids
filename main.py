import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    

    updatable = [player]
    drawable = [player]

    # Create a new AsteroidField object
    asteroid_field = AsteroidField()
    updatable.append(asteroid_field)
    drawable.append(asteroid_field)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

        # Draw all drawable objects
        screen.fill((0, 0, 0))  # Fill the screen with black
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # Update the full display Surface to the screen

    pygame.quit()

if __name__ == "__main__":
    main()