import pygame
from Skynet import Skynet

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Plane Game")

# object setup
numDataPointsX = 500  # number of points in x direction
numDataPointsY = 300  # number of points in y direction
spacing = 10  # space between points

# create a list of tuples (2 numbers)
datapoints = []

# Create grid points
for x in range(1, 1000, spacing * 2):
    for y in range(1, 600, spacing * 2):
        datapoints.append((x, y))

# Create new Network and train it
skynet = Skynet([2, 3, 2])


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from the last frame
    screen.fill("white")
    
    # Train the network
    skynet.learn(datapoints, 0.1)
    

    # display the datapoints
    for point in datapoints:
        # Call AI classify
        index = skynet.classify(point)
        if index == 0:
            pygame.draw.circle(screen, "purple", (point[0], point[1]), 4)
        
        if point[1] < (point[0] ** 2) / 2000:
            pygame.draw.circle(screen, "green", (point[0], point[1]), 2)
        else:
            pygame.draw.circle(screen, "red", (point[0], point[1]), 2)
        

    # draw function
    for x in range(1, 1000):
        y = (x ** 2) / 2000  # scale down the y-values to fit the screen height
        if y < 600:  # make sure y is within the screen height
            pygame.draw.circle(screen, "black", (x, int(y)), 1)

    # flip the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()
