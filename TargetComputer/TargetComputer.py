from cgi import test
import pygame

# Import object classes
from Plane import Plane
from Cannon import Cannon
from Projectile import Projectile
from Simple import Simple
from SimpleOptimized import SimpleOptimized

# random float 


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Plane Game")

# object setup
plane = Plane()
plane2 = Plane()
cannon = Cannon(500, 550)
projectile = None
plane.setRandomPath()
plane2.setRandomPath()
# Random Path with -1 to 1
hitpos = (0, 0)
shot = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    # function calls
    
    if not shot:
        # Plane 1 / Simple
        simple = Simple(cannon.x, cannon.y, plane)
        simple.find_hitpoint()
        projectile = cannon.shoot(simple.hitpoint_x, simple.hitpoint_y, 1)
        hitpos = (simple.hitpoint_x, simple.hitpoint_y)
        print (simple.hitpoint_x, simple.hitpoint_y)
        
        # Plane 2 / Simple Optimized
        simple2 = SimpleOptimized(cannon.x, cannon.y, plane2)
        simple2.find_hitpoint()
        projectile2 = cannon.shoot(simple2.hitpoint_x, simple2.hitpoint_y, 1)
        hitpos = (simple2.hitpoint_x, simple2.hitpoint_y)
        print (simple2.hitpoint_x, simple2.hitpoint_y)
        
        shot = True
        
    #simple3 = Simple(cannon.x, cannon.y, plane)
    #simple3.find_hitpoint()
    
    # move function calls
    projectile.move(1)
    projectile2.move(1)
    plane.move()
    plane2.move()
    
    # RENDER YOUR GAME HERE
    # Plane 1
    screen.blit(pygame.transform.flip(plane.img, True, False), (plane.x, plane.y))
    pygame.draw.circle(screen, "black", (plane.x, plane.y), 6)
    screen.blit(cannon.img, (cannon.x, cannon.y))
    pygame.draw.circle(screen, "red", (projectile.x, projectile.y), 6)
    
    # Plane 2
    screen.blit(pygame.transform.flip(plane2.img, True, False), (plane2.x, plane2.y))
    pygame.draw.circle(screen, "black", (plane2.x, plane2.y), 6)
    screen.blit(cannon.img, (cannon.x, cannon.y))
    pygame.draw.circle(screen, "red", (projectile2.x, projectile2.y), 6)    
    
    #pygame.draw.circle(screen, "green", (simple2.hitpoint_x, simple2.hitpoint_y), 10)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()