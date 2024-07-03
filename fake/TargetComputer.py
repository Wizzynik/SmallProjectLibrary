import pygame

# Import object classes
from Plane import Plane
from Cannon import Cannon
from Projectile import Projectile

# random float 
from random import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Plane Game")

# object setup
plane = Plane()
cannon = Cannon()
projectile = cannon.shoot(1000, 300)
# Random Path with -1 to 1
randomPath = (random()*2 - 1) *0.4

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    # function
    plane.move(1,randomPath)
    projectile.move()
    
    # RENDER YOUR GAME HERE
    screen.blit(pygame.transform.flip(plane.img, True, False), (plane.x, plane.y))
    screen.blit(cannon.img, (cannon.x, cannon.y))
    pygame.draw.circle(screen, "red", (projectile.x, projectile.y), 10)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()