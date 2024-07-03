import pygame

from random import random
# Plane Class
class Plane:
    x = 0
    y = 200
    randomPath = 0

    img = pygame.transform.scale(pygame.image.load("fake/assets/plane.png"), (60, 40))
    
    def move(self):
        self.x += 1
        self.y += self.randomPath

    def setRandomPath(self):
        self.randomPath = (random()*2 - 1) *0.4