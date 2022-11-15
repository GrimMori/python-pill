import os
import sys

import pygame
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()

# to do:
# make window size adaptable to screen size
# make image centered on window

sw = pygame.display.get_desktop_sizes()[0][0] # get width of the screen
sh = pygame.display.get_desktop_sizes()[0][1] # get height of the screen
screensize = (sw, sh) # size of the screen

surface = pygame.display.set_mode(screensize) #opens up a window
icon = pygame.image.load('icon.png') # loads an image
pygame.display.set_icon(icon) # uses loaded image as icon for the window


folder = "slides/" # folder that contains the slides
files = [] # new list that will contain the slides

# use extend instead of append. append would add the whole list to the first index of 'files'. 
# but we want each element of the list to be added to each new index of 'files'.
files.extend(os.listdir(folder))
files.sort() # sorts the list in ascending order (alphabetical by default)
x = 0

# load images

while True:
    for event in pygame.event.get(): # handle inputs
        if event.type == QUIT: # quit (close window) input
            pygame.quit()
            sys.exit() # close window
        if event.type == MOUSEBUTTONDOWN: # when mouse is clicked
            if x < len(files)-1:
                x += 1 
                path = folder + files[x]
                img = pygame.image.load(path)
                print(files[x])
                print(str(path))
                
            else:
                print("end!")
        
            img_x = (sw/2 - img.get_width()/2) # centered width
            img_y = (sh/2 - img.get_height()/2) # centered height
            print(img_x, img_y)
            surface.blit(img, (img_x, img_y)) # render the image, centered
    pygame.display.update()
    fpsClock.tick(30)
    
    
    
    
    
    
    
    
    
    
    
    