from universal import *
from variables import *

# Draw DAS Box for Input
def drawdasbox(screen, invalidnum, userdas): 
    input_rectnum = pygame.Rect(coordconverter(500, pygame.display.Info().current_w), coordconverter(500, pygame.display.Info().current_w), coordconverter(140, pygame.display.Info().current_w), coordconverter(50, pygame.display.Info().current_w))
    # Display prompt for DAS input
    screen.blit(gamefont(coordconverter(60, pygame.display.Info().current_w)).render("Input DAS in ms. (enter) to submit", True, BLACK), (coordconverter(230, pygame.display.Info().current_w), coordconverter(400, pygame.display.Info().current_w)))
    # Draw the input box
    pygame.draw.rect(screen, pygame.Color('lightskyblue3'), input_rectnum)
    # Render the user-entered DAS value
    screen.blit(gamefont(coordconverter(40, pygame.display.Info().current_w)).render(userdas, True, pygame.Color('black')), (input_rectnum.x+coordconverter(5, pygame.display.Info().current_w), input_rectnum.y+coordconverter(3, pygame.display.Info().current_w)))
    # Adjust the input box width dynamically based on text
    input_rectnum.w = max(100, gamefont(coordconverter(20, pygame.display.Info().current_w)).size(userdas)[0] + coordconverter(10, pygame.display.Info().current_w))
    # Display error message if the input is invalid
    if invalidnum:
        screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render("Invalid number", True, RED), (input_rectnum.x + coordconverter(5, pygame.display.Info().current_w), input_rectnum.y + input_rectnum.height + coordconverter(5, pygame.display.Info().current_w)))

# Draw Algorithm Input Box
def algbox(screen, invalidnotation, useralg):
    input_rectalg = pygame.Rect(coordconverter(700, pygame.display.Info().current_w), coordconverter(550, pygame.display.Info().current_w), coordconverter(140, pygame.display.Info().current_w), coordconverter(25, pygame.display.Info().current_w))
    # Draw the algorithm input box
    # Adjust the input box width dynamically
    input_rectalg.w = max(coordconverter(50, pygame.display.Info().current_w), gamefont(coordconverter(20, pygame.display.Info().current_w)).size(useralg)[0]+coordconverter(20, pygame.display.Info().current_w))
    pygame.draw.rect(screen, pygame.Color('lightskyblue3'), input_rectalg)
    # Render the user-entered algorithm
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render(useralg, True, BLACK), (input_rectalg.x+coordconverter(5, pygame.display.Info().current_w), input_rectalg.y+coordconverter(3, pygame.display.Info().current_w)))
    # Display error message if the algorithm notation is invalid
    if invalidnotation:
        screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render("Invalid input", True, RED), (input_rectalg.x + coordconverter(5, pygame.display.Info().current_w), input_rectalg.y + input_rectalg.height + 5))
    # Draw the algorithm input box
    # Adjust the input box width dynamically
    input_rectalg.w = max(coordconverter(50, pygame.display.Info().current_w), algfont().size(useralg)[0]+coordconverter(20, pygame.display.Info().current_w))
    pygame.draw.rect(screen, pygame.Color('lightskyblue3'), input_rectalg)
    # Render the user-entered algorithm
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render(useralg, True, BLACK, None), (input_rectalg.x+coordconverter(5, pygame.display.Info().current_w), input_rectalg.y+coordconverter(3, pygame.display.Info().current_w)))
    # Display error message if the algorithm notation is invalid
