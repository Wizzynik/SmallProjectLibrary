import pygame

# Import object classes
from template.Plane1 import Plane

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Plane Game")

# object setup
plane = Plane()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    # function
    plane.move(1,0)
    
    # RENDER YOUR GAME HERE
    screen.blit(pygame.transform.flip(plane.img, True, False), (plane.x, plane.y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(5)  # limits FPS to 60

pygame.quit()