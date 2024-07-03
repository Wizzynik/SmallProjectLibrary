import pygame
from Projectile import Projectile

# Cannon Class
class Cannon:
    x = 500
    y = 550

    img = pygame.transform.scale(pygame.image.load("fake/assets/cannon.jpg"), (50, 50))
    
    def move(self, x, y):
        self.x += x
        self.y += y
        
    def shoot(self, hitX, hitY):
        # use class attributes
        if hitX - self.x == 0:
            slope = 0
        else:
            slope =  (hitX - self.x) / (hitY - self.y)
        return Projectile(self.x, self.y, slope)