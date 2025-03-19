from variables import *
from universal import *
import math

# Practice stuff
def practice_words(screen):
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render("(esc) to reset cube", True, BLACK), (coordconverter(1150, pygame.display.Info().current_w), coordconverter(30, pygame.display.Info().current_w)))

# Draw the Rubik's cube state using the cube variable
def drawcube(screen, cube):
    # Define the cube's coordinates
    leftcoor = int(coordconverter(70, pygame.display.Info().current_w))
    topcoor = int(coordconverter(240, pygame.display.Info().current_w))
    slantlength = coordconverter((int(math.sqrt(1400*1400 + 900*900) / (math.sqrt(1400*1400 + 900*900)/180))), pygame.display.Info().current_w)
    oneslant = slantlength / 3
    regwidth = coordconverter(300, pygame.display.Info().current_w)
    regheight = coordconverter(300, pygame.display.Info().current_w)
    onewidth = regwidth / 3
    oneheight = regheight / 3
    xcoords = [leftcoor + slantlength + regwidth, leftcoor, leftcoor + regwidth, leftcoor + 2 * regwidth, leftcoor + regwidth, leftcoor + regwidth * 2 + slantlength]
    ycoords = [topcoor - slantlength, topcoor, topcoor, topcoor, topcoor + regheight, topcoor - slantlength]
    heights = [oneslant, oneheight, oneheight, oneheight, oneheight, oneheight]
    widths = [onewidth, onewidth, onewidth, oneslant, onewidth, onewidth]
    dispx = [-1 * oneslant, 0, 0, 0, 0, 0]
    dispy = [0, 0, 0, -1 * oneslant, 0, 0]
    for k in range(6):
        for i in range(3):
            for j in range(3):
                color = cube[k][i][j]
                x = widths[k] * i + xcoords[k]
                y = heights[k] * j + ycoords[k]
                width = widths[k]
                height = heights[k]
                points = [
                    [x + dispx[k] * j, y + dispy[k] * i],
                    [x + width + dispx[k] * j, y + dispy[k] + dispy[k] * i],
                    [x + width + dispx[k] + dispx[k] * j, y + height + dispy[k] + dispy[k] * i],
                    [x + dispx[k] + dispx[k] * j, y + height + dispy[k] * i]
                ]
                pygame.draw.polygon(screen, color, points)
                pygame.draw.polygon(screen, BLACK, points, 2)
    return cube