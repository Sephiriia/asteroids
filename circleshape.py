import pygame
import sys

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # No-op for base class
        pass

    def update(self, dt):
        # Move the circle by its velocity
        self.position += self.velocity * dt

    def collisions(self, other):
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)

    def check_collision(self, other):
        return self.collisions(other)