import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_NEW_SPEED_SCALE, \
    WHITE_COLOR, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, WHITE_COLOR, self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
        # uncomment to let asteroids wrap around
        # super().update(dt)
    
    def split(self):
        self.kill()

        # do not split small asteroids below min radius
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = self.velocity.rotate(random_angle) * ASTEROID_NEW_SPEED_SCALE
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = self.velocity.rotate(-random_angle)