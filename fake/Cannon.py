import pygame
import math
from Projectile import Projectile

class Cannon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.transform.scale(pygame.image.load("fake/assets/cannon.jpg"), (50, 50))
    
    def move(self, x, y):
        self.x += x
        self.y += y
        
    def shoot(self, target_x, target_y, velocity):
        dx = target_x - self.x
        dy = self.y - target_y  # Umgekehrt, da y nach unten zunimmt
        angle = math.degrees(math.atan2(dy, dx))
        return Projectile(self.x, self.y, angle, velocity)