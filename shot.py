from circleshape import CircleShape
from constants import SHOT_RADIUS, WHITE_COLOR, LINE_WIDTH
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,SHOT_RADIUS)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, WHITE_COLOR, self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt