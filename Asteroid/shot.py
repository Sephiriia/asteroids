from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
    containers = []

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.velocity = pygame.Vector2(0, 0)
        self.image = pygame.Surface((2 * SHOT_RADIUS, 2 * SHOT_RADIUS), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))