import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_NEW_SPEED_SCALE

class Asteroid(CircleShape):
    def __init__(self, x, y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        # sub-classes must override
        white_color = [255,255,255]
        line_width = 2
        pygame.draw.circle(screen, white_color, self.position, self.radius, line_width)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = self.velocity.rotate(random_angle) * ASTEROID_NEW_SPEED_SCALE
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = self.velocity.rotate(-random_angle)