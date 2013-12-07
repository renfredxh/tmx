tmx
===

This is an official fork and python 3 port of the [pygame tmx library originally](https://bitbucket.org/r1chardj0n3s/pygame-tutorial/src/995c364f087cc24e20682f642b3b406e7e3dcdae/tmx.py) made by [Richard Jones](https://bitbucket.org/r1chardj0n3s). 

Tmx is a powerful [tmx-based](https://github.com/bjorn/tiled/wiki/TMX-Map-Format) tile engine for pygame that allows for simple and fast animating of tile based maps and/or sprites. TMX maps are flexible XML files can be eaisly developed and edited using a [GUI tilemap editor](http://www.mapeditor.org/) and used to describe a tile based map with any tile size, any amount of layers, any number of tile sets and it allows custom properties to be set on most elements. For more information on how to use a tilemap editor, [check out this tutorial](http://gamedev.tutsplus.com/tutorials/level-design/introduction-to-tiled-map-editor/).

I've decided to fork this so that people that would like to use python 3 to develop tiled based games will have access to compatible tools. If you'd still like to use python 2.x, you can use the [python 2.x branch](https://github.com/RenfredH04/tmx/tree/python2.x).
There is no offical doumentation for tmx yet, but you can view an example of pratical use of this library in my project, [pylletTown](https://github.com/RenfredH04/pylletTown) along with a [video of it working in action](http://youtu.be/KnOMXyqbxqY).
Also included is a folder of [various examples](https://github.com/RenfredH04/tmx#running-examples) of different kinds of game to show what the library is capable of. 

Installiation of the [pygame](http://www.pygame.org/install.html) and any version of [python3](http://www.python.org/getit/) is required to use tmx.

## Getting Started

Below is a short annoted example that contains the bare minimum amount of code to get a tmx map up and running. Feel free to copy and paste it to play around with it or use it to learn more about each method.

```python
import pygame
import tmx

# Initialize pygame and create a 500x500 display.
pygame.init()
screen = pygame.display.set_mode((500 , 500))

# tmx.load parses the myMap.tmx file and returns a tilemap with all of
# the appropriate attributes. Note you must also include the viewport size. 
tilemap = tmx.load('myMap.tmx', screen.get_size())

# You must set the focus of the tilemap view to an x, y coordinate. This 
# tells the tmx library where to center its view. Usually this would be set 
# to the starting position of the main player's sprite.
tilemap.set_focus(0, 0)
clock = pygame.time.Clock()

# Main game loop
while 1:
    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # tilemap.update calls the update method on each layer in the map.
    # The update method can be customized for each layer to include logic
    # for animating sprite positions, and detecting collisions.              
    tilemap.update(dt)
    # Fill the screen with an R,G,B color to erase the previous drawings.
    screen.fill((0,0,0))
    # Draw all layers of the tilemap to the screen.
    tilemap.draw(screen)
    # Refresh the display window. 
    pygame.display.flip()
```

## Running Examples

Make sure you are in the examples directory, then run the python file of the example you'd like to see.

    $ cd tmx/examples
    $ python3 simpleDemo.py
    


