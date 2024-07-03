import pygame
# Plane Class
class Plane:
    x = 0
    y = 200

    img = pygame.transform.scale(pygame.image.load("fake/assets/plane.png"), (60, 40))
    
    def move(self, x, y):
        self.x += x
        self.y += y