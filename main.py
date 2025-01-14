import pygame
import sys
import random
from player import Player
from asteroid import Asteroid
from shot import Shot

def spawn_asteroid(asteroids):
    position = (random.randint(0, screen_width), random.randint(0, screen_height))
    size = (random.randint(20, 50), random.randint(20, 50))  # Example size
    asteroid = Asteroid(position, size)
    asteroids.add(asteroid)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    print("Starting asteroids!")
    print(f"Screen width: {screen.get_width()}")
    print(f"Screen height: {screen.get_height()}")

    drawable = []
    updatable = []

    # Create player and asteroids group
    player = Player(400, 300)
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = asteroids
    Shot.containers = shots

    # Initial spawn of asteroids
    for _ in range(5):
        spawn_asteroid(asteroids)

    drawable.append(player)
    drawable.extend(asteroids)
    drawable.extend(shots)
    updatable.append(player)
    updatable.extend(asteroids)
    updatable.extend(shots)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                running = False
                break

        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for shot in player.shots:
                if pygame.sprite.collide_rect(asteroid, shot):
                    asteroid.kill()
                    shot.kill()

        # Draw all drawable objects
        screen.fill((0, 0, 0))  # Fill the screen with black
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # Update the full display Surface to the screen

        # Spawn new asteroids periodically
        if random.random() < 0.01:  # Adjust the probability as needed
            spawn_asteroid(asteroids)
            drawable.append(asteroids.sprites()[-1])
            updatable.append(asteroids.sprites()[-1])

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()