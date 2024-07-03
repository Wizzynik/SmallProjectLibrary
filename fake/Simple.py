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
            current_plane_x = self.plane_start_x + range * self.plane_velocity
            current_plane_y = self.plane_start_y + range * self.plane_velocity
            plane_distance = math.sqrt((self.start_x - current_plane_x)**2 + (self.start_y - current_plane_y)**2)
            projectile_distance = range * self.velocity;            
        
            print ("Range: ", range)
            print ("Plane Distance: ", plane_distance)
            print ("Projectile Distance: ", projectile_distance)
    
            if(plane_distance <= projectile_distance):
                self.hitpoint_x = range * self.velocity
                self.hitpoint_y = range * self.velocity
                break
            range = range + 1
            
    