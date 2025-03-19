from universal import *
from variables import *

# alg calculator stuff
def algcalc_words(screen, analysis):
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render("(esc) to exit algorithm calculator", True, BLACK), (coordconverter(500, pygame.display.Info().current_w), coordconverter(30, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(40, pygame.display.Info().current_w)).render("Input custom alg.", True, BLACK), (coordconverter(850, pygame.display.Info().current_w), coordconverter(400, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(40, pygame.display.Info().current_w)).render("(enter) to submit", True, BLACK), (coordconverter(800, pygame.display.Info().current_w), coordconverter(450, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render("Prime (') denoted by 'p'", True, BLACK), (coordconverter(750, pygame.display.Info().current_w), coordconverter(500, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(15, pygame.display.Info().current_w)).render("Moves must be separated by space", True, BLACK), (coordconverter(750, pygame.display.Info().current_w), coordconverter(525, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render("(\\) to reset cube", True, BLACK), (coordconverter(1200, pygame.display.Info().current_w), coordconverter(30, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render(f"SHTM: {analysis[0]}", True, BLACK), (coordconverter(814, pygame.display.Info().current_w), coordconverter(610, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render(f"Cube rotations: {analysis[1]}", True, BLACK), (coordconverter(725, pygame.display.Info().current_w), coordconverter(660, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render(f"Double: {analysis[2]}", True, BLACK), (coordconverter(798, pygame.display.Info().current_w), coordconverter(710, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render(f"Slice: {analysis[3]}", True, BLACK), (coordconverter(825, pygame.display.Info().current_w), coordconverter(760, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render(f"Simult: {analysis[4]}", True, BLACK), (coordconverter(805, pygame.display.Info().current_w), coordconverter(810, pygame.display.Info().current_w)))
    if analysis[5] == 0:
        string = "-"
    else:
        string = str(round(float(analysis[0]) / float(analysis[5]) * 100, 2))
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render(f"Efficiency: {string}%", True, BLACK), (coordconverter(1000, pygame.display.Info().current_w), coordconverter(660, pygame.display.Info().current_w)))

# Analyze Move Sequences
def move_analyzer(moves):
    # Initialize metrics for analyzing moves: 
    # SHTM (Single-Hand Turns), hard regrips, doubles, slices, and simultaneous moves
    info = [0, 0, 0, 0, 0, 0]
    # Weights for scoring moves (adjust as needed for your use case)
    weights = [1, 2, 0.5, 0.1, -1]
    prevmove = ""
    
    for move in moves:
        if move in "xyzXYZ":  # Check if the move is a regrip
            info[1] += 1
        else:
            info[0] += 1  # Increment SHTM for standard moves
            if move.endswith("2"):  # Check for double moves
                info[2] += 1
            if move in "MESmesrudfbl":  # Check for slice moves
                info[3] += 1
            elif prevmove + move in ["RL", "LR", "UD", "DU", "FB", "BF"]:  # Check for simult
                info[4] += 1
        prevmove = move
    # Calculate the total score using weights
    info[5] = sum([info[i] * weights[i] for i in range(5)])
    return info
