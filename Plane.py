import pygame
# Plane Class
class Plane:
    x = 0
    y = 0

    img = pygame.transform.scale(pygame.image.load("plane.png"), (60, 40))
    
    
    def move(self):
        self.x += 1
        self.y += 1