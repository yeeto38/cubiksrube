from variables import *
from universal import *

# Draw the menu
def drawmenu(screen, hover):
    screen.blit(gamefont(coordconverter(25, pygame.display.Info().current_w)).render("(r)esize", True, BLACK), (coordconverter(1300, pygame.display.Info().current_w), coordconverter(20, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(60, pygame.display.Info().current_w)).render("MENU", True, BLACK), (coordconverter(600, pygame.display.Info().current_w), coordconverter(250, pygame.display.Info().current_w)))
    for i in range(len(menu_options())):
        color = RED if i == hover else BLACK
        screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render(menu_options()[i], True, color), (coordconverter(600, pygame.display.Info().current_w), coordconverter(350, pygame.display.Info().current_w) + (i * coordconverter(40, pygame.display.Info().current_w))))

# Keybinds Words Renderer
def keybinds_words(screen):
    # Render the keybinds text on the screen.
    screen.blit(gamefont(coordconverter(26, pygame.display.Info().current_w)).render("keybinds (-)", True, BLACK), (coordconverter(20, pygame.display.Info().current_w), coordconverter(190, pygame.display.Info().current_w)))

# Write the permanent text
def permtext(screen):
    screen.blit(gamefont(coordconverter(48, pygame.display.Info().current_w)).render("Rubik's Cube", True, BLACK), (coordconverter(20, pygame.display.Info().current_w), coordconverter(20, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(48, pygame.display.Info().current_w)).render("Utility", True, BLACK), (coordconverter(20, pygame.display.Info().current_w), coordconverter(72, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(26, pygame.display.Info().current_w)).render("menu (=)", True, BLACK), (coordconverter(20, pygame.display.Info().current_w), coordconverter(140, pygame.display.Info().current_w)))
