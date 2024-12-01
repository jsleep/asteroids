import pygame

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_ACCELERATE, \
    PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, \
    LINE_WIDTH, WHITE_COLOR
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.speed = 0
        self.acceleration = 0
    
    # return triangle points of player circle shape
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, WHITE_COLOR, self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def accelerate(self,dt):
        self.acceleration += 1 if dt > 0 else -1

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * self.acceleration * dt * PLAYER_ACCELERATE
        self.position += self.velocity * dt
    
    def shoot(self):
        if self.shoot_timer < 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
    
    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        # rotate with A or D
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        # accelerate with W or decelerate with S
        if keys[pygame.K_w]:
            self.accelerate(dt)
        if keys[pygame.K_s]:
            self.accelerate(-dt)
        
        # always move now that we are only directly controlling acceleration
        self.move(dt)
        
        # shoot
        if keys[pygame.K_SPACE]:
            self.shoot()