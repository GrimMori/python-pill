import os
import sys

import pygame
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()
window = (800, 600) # size of the window
surface = pygame.display.set_mode(window) #opens up a window
icon = pygame.image.load('../yippee.jpeg') # loads an image
pygame.display.set_icon(icon) # uses image as icon for the window


folder = "slides/" # folder that contains the slides
files = [] # new list that will contain the slides

# use extend instead of append. append would add the whole list to the first index of 'files'. 
# but we want each element of the list to be added to each new index of 'files'.
files.extend(os.listdir(folder))
files.sort() # sorts the list in ascending order (alphabetical by default)



while True:
    for event in pygame.event.get(): # handle inputs
        if event.type == QUIT: 
            pygame.quit()
            sys.exit() # close window
        if event.type == MOUSEBUTTONDOWN: # when mouse is clicked
            print(files)
        
    pygame.display.update()
    fpsClock.tick(30)