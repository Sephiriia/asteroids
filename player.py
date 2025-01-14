import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.rotation = 0
        self.shots = pygame.sprite.Group()
        self.shoot_timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    
    
    def draw(self, screen):
        vertices = self.triangle()
        color = (255, 255, 255)
        pygame.draw.polygon(screen, color, vertices, 2)
        for shot in self.shots:
            shot.draw(screen)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)

        # Decrease the shoot timer by dt
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        # Prevent shooting if the timer is greater than 0
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            shot = self.shoot()
            if shot:  # Ensure the shot is not None
                self.shots.add(shot)
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset the timer after shooting

        for shot in self.shots:
            shot.update(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_position = self.position + forward * self.radius
        shot = Shot(shot_position.x, shot_position.y)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        return shot