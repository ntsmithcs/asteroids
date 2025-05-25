from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        trajectory_left = self.velocity.rotate(-random_angle)
        trajectory_right = self.velocity.rotate(random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_left = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_right = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_left.velocity = trajectory_left * 1.2
        new_asteroid_right.velocity = trajectory_right * 1.2

        

