from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame

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