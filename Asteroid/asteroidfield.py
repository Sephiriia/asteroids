import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField:
    containers = None
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        self.asteroids = pygame.sprite.Group()
        Asteroid.containers = self.asteroids
        self.spawn_timer = 0

    def spawn_asteroid(self):
        edge = random.choice(self.edges)
        position = edge[1](random.random())
        velocity = edge[0] * random.uniform(50, 150)
        radius = random.randint(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS)
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        self.asteroids.add(asteroid)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer >= ASTEROID_SPAWN_RATE:
            self.spawn_asteroid()
            self.spawn_timer = 0
        self.asteroids.update(dt)

    def draw(self, screen):
        self.asteroids.draw(screen)