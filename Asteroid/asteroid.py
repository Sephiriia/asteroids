from circleshape import CircleShape
import pygame

class Asteroid:
    containers = []

    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.velocity = pygame.Vector2(0, 0)
        self.image = pygame.Surface((2 * size, 2 * size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (size, size), size, 2)
        self.rect = self.image.get_rect(center=(position.x, position.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))