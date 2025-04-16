import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import *

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont('Comic Sans MS', 35)
    dt = 0
    score = 0
    

    # groups
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    blasts = pygame.sprite.Group()

    # containers
    Player.containers = (drawable, updatable)
    Shot.containers = (shots, drawable, updatable)
    Blast.containers = (blasts, drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable

    # create asteroid field and player
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    
    
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        # check for player and asteroid collisions
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over!")
                return
        
        # check for shot and asteroid collisions
        for asteroid in asteroids:
            for shot in shots:
                if (shot.collision(asteroid) == True):
                    score += 1
                    asteroid.split()
                    shot.kill()

        for asteroid in asteroids:
            for blast in blasts:
                if (blast.collision(asteroid) == True):
                    score += 1
                    asteroid.split()
                    blast.split()
        
        # fill screen black
        screen.fill("black")
        
        text_surface = my_font.render(f"Score: {score}", False, (255, 255, 255))
        screen.blit(text_surface, (0,0))

        # draw objects
        for obj in drawable:
            obj.draw(screen)

        # update full display surface to the screen
        pygame.display.flip()

        # controls games framerate to 60
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
