# Demo written by RenfredH04
exec(open("importer.py").read()) # Add tmx to path (ignore this)

import pygame
import tmx

# Initialize pygame and create a 500x500 display 
pygame.init()
screen = pygame.display.set_mode((500 , 500))

# tmx.load parses the myMap.tmx file and returns a tilemap with all of
# the appropriate attributes. Note you must also include the viewport size. 
tilemap = tmx.load('simpleDemo.tmx', screen.get_size())

# Set the focus of the tilemap view to an x, y coordinate. Usually this
# would be set to the starting position of the main player's sprite.
tilemap.set_focus(0, 0)
clock = pygame.time.Clock()

while 1:
    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # tilemap.update calls the update method on each layer in the map.
    # The update method can be customized for each layer to include logic
    # for animating sprite positions, and detecting collisions .              
    tilemap.update(dt)
    # Fill the screen with an R,G,B color to erase the previous drawings
    screen.fill((0,0,0))
    # Draw all layers of the tilemap to the screen.
    tilemap.draw(screen)
    # Refresh the display window. 
    pygame.display.flip()