import pygame

# Projectile Class
class Projectile:
    x = 0
    y = 0
    slope = 0
    
    def __init__(self, x, y, slope):
        self.x = x
        self.y = y
        self.slope = -slope
    
    def move(self):
        self.x += self.slope
        self.y += -1