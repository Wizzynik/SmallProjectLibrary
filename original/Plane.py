import pygame
from random import randint
# Plane Class
class Plane:
    x = 0
    y = randint(100, 300)

    img = pygame.transform.scale(pygame.image.load("original/plane.png"), (60, 40))
    
    
    def move(self, x, y):
        self.x += x
        self.y += y