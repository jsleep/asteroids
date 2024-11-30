# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print('Starting asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        black_color = [0,0,0]
        screen.fill(black_color)
        
        for u in updatable:
            u.update(dt)
        
        for d in drawable:
            d.draw(screen)
        
        for a in asteroids:
            if a.collision(player):
                print('Game over!')
                sys.exit(1)
            
            for s in shots:
                if a.collision(s):
                    a.kill()
                    s.kill()


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()