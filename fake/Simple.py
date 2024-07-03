# Simple targeting algorithm
import math
from Plane import Plane

class Simple:
    start_x = 0
    start_y = 0
    velocity = 1

    plane_start_x = None
    plane_start_y = None
    plane_direction = None
    plane_velocity = None
    plane = None

    hitpoint_x = 0
    hitpoint_y = 0

    def __init__(self, x, y, plane):
        self.start_x = x
        self.start_y = y

        self.plane = plane
        self.plane_start_x = plane.x
        self.plane_start_y = plane.y
        self.plane_direction = plane.randomPath
        self.plane_velocity = math.sqrt(1 + plane.randomPath**2)

    def find_hitpoint(self):
        range = 0
        while(range <= 1000):
            if(self.plane_start_x + range * self.plane_velocity <= self.start_x + range * self.velocity and self.plane_start_y + range * self.plane_velocity <= self.start_y + range * self.velocity):
                self.hitpoint_x = range * self.velocity
                self.hitpoint_y = range * self.velocity
            range = range + 1
            
    