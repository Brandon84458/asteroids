import pygame
from constants import *
from circleshape import CircleShape
import random


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

class Blast(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "orange", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * 0.75*dt

    def split(self):
        self.kill()
        if self.radius <= BLAST_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)
            vector3 = self.velocity.rotate(random.uniform(20,50) + random_angle)
            vector4 = self.velocity.rotate(random.uniform(20,50) + -random_angle)
            
            new_radius = self.radius - BLAST_MIN_RADIUS

            new_asteroid1 = Blast(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = vector1 * random.uniform(1,2)
            new_asteroid2 = Blast(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = vector2 * random.uniform(1,2)
            new_asteroid3 = Blast(self.position.x, self.position.y, new_radius)
            new_asteroid3.velocity = vector3 * random.uniform(1,2)
            new_asteroid4 = Blast(self.position.x, self.position.y, new_radius)
            new_asteroid4.velocity = vector4 * random.uniform(1,2)