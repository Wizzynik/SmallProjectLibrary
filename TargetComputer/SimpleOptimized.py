# Simple targeting algorithm
import math
from Plane import Plane

class SimpleOptimized:
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
        
    def calc_distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def find_hitpoint(self, accuracy = 0.1, max_Iterations = 1000):
        left = 0
        right = self.calc_distance(self.start_x, self.start_y, self.plane_start_x, self.plane_start_y)
        
        steps = 0 # Counter for steps
        for _ in range(max_Iterations):
            steps += 1 # Counter for steps
            
            mid = (left + right) / 2
            
            current_plane_x = self.plane_start_x + mid * self.plane_velocity
            current_plane_y = self.plane_start_y + mid * self.plane_direction
            
            plane_distance = self.calc_distance(self.start_x, self.start_y, current_plane_x, current_plane_y)
            projectile_distance = mid * self.velocity
            
            if abs(plane_distance - projectile_distance) <= accuracy:
                self.hitpoint_x = current_plane_x
                self.hitpoint_y = current_plane_y
                print ("Simple Optimized Steps: ", steps)
                return True # Hitpoint found
            
            if plane_distance > projectile_distance:
                left = mid
            else:
                right = mid
                
        return False # No hitpoint found
                