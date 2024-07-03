import math

class Projectile:
    def __init__(self, x, y, angle, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.angle = math.radians(angle)  # Winkel in Radianten umwandeln
        self.vx = velocity * math.cos(self.angle)
        self.vy = -velocity * math.sin(self.angle)  # Negative, weil y nach unten zunimmt
    
    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt