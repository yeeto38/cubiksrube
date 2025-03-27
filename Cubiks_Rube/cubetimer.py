from variables import *
from universal import *
import random

def genscramble():
    smoves = ["R", "U", "F", "L", "D", "B", "R'", "U'", "F'", "L'", "D'", "B'", "R2", "U2", "F2", "L2", "D2", "B2"]
    out = []
    prev = 0
    curr = 0
    # Generate 20 random moves
    for _ in range(20):
        # Make sure the next move is not the same as the previous
        curr = random.randint(0, len(smoves)-1)
        if len(out) <= 1:
            while len(out) > 0 and curr % 6 == prev % 6:
                curr = (curr + 1) % len(smoves)
        else:
            while (len(out) > 0 and curr % 6 == prev % 6) or same_move(out[-2], out[-1], smoves[curr]):
                curr = (curr + 1) % len(smoves)
        out.append(smoves[curr])
        prev = curr % 6
    return out

def same_move(move1, move2, move3):
    x = ["R", "R'", "R2", "L", "L'", "L2"]
    y = ["U", "U'", "U2", "D", "D'", "D2"]
    z = ["F", "F'", "F2", "B", "B'", "B2"]
    return ((move1 in x and move2 in x and move3 in x) or
            (move1 in y and move2 in y and move3 in y) or
            (move1 in z and move2 in z and move3 in z))

def scramb(scramble):
    moves = splitmoves(" ".join(scramble))
    cube = defstate()
    for move in moves:
        move_to_action(move)(cube)
    return cube

def solved(cube):
    # Iterate through all cube faces to check if each face is a solid color
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if cube[i][j][k] != cube[i][1][1]:
                    return False
    return True

# Timer stuff
def timer_words(screen, times, currtime, color, scramble, virtual_solving):
    # splits scramble into 2 lines
    first_ten_moves = scramble[:9]
    last_ten_moves = scramble[9:]
    first_ten_moves = " ".join(first_ten_moves)
    last_ten_moves = " ".join(last_ten_moves)
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render("(esc) to reset timer", True, BLACK), (coordconverter(1150, pygame.display.Info().current_w), coordconverter(30, pygame.display.Info().current_w)))
    # display the last 5 times
    for i in range(5):
        time_text = f"{i+1}     {(times[i]/1000):.3f}" if times[i] != 0 else f"{i+1}     ---"
        screen.blit(gamefont(coordconverter(25, pygame.display.Info().current_w)).render(time_text, True, BLACK), (coordconverter(120, pygame.display.Info().current_w), coordconverter(670, pygame.display.Info().current_w)+(coordconverter(40, pygame.display.Info().current_w)*i)))
    valid_times = [time for time in times if time != 0]
    # calculate ao5
    ao5x=85
    ao5y=570
    if len(valid_times) >= 5:
        sorted_times = sorted(valid_times[:5])
        ao5 = sum(sorted_times[1:4]) / 3
        if ao5 > 60000:
            min = int(ao5 / 60000)
            sec = ((ao5 - min * 60000) / 1000)
            screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render(f"AO5: {(min)}:{(sec):0.3f}", True, BLACK), (coordconverter(ao5x, pygame.display.Info().current_w), coordconverter(ao5y, pygame.display.Info().current_w)))
        else:
            screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render(f"AO5: {(ao5/1000):.3f}", True, BLACK), (coordconverter(ao5x, pygame.display.Info().current_w), coordconverter(ao5y, pygame.display.Info().current_w)))
    else:
        screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render("AO5: ---", True, BLACK), (coordconverter(ao5x, pygame.display.Info().current_w), coordconverter(ao5y, pygame.display.Info().current_w)))
    # calculate ao12
    ao12x=ao5x-18
    ao12y=ao5y+50
    if len(valid_times) >= 12:
        sorted_times = sorted(valid_times[:12])
        ao12 = sum(sorted_times[1:11]) / 10
        if ao12 > 60000:
            min = int(ao12 / 60000)
            sec = ((ao12 - min * 60000) / 1000)
            screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render(f"AO12: {(min)}:{(sec):0.3f}", True, BLACK), (coordconverter(ao12x, pygame.display.Info().current_w), coordconverter(ao12y, pygame.display.Info().current_w)))
        else:
            screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render(f"AO12: {(ao12/1000):0.3f}", True, BLACK), (coordconverter(ao12x, pygame.display.Info().current_w), coordconverter(ao12y, pygame.display.Info().current_w)))
    else:
        screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render("AO12: ---", True, BLACK), (coordconverter(ao12x, pygame.display.Info().current_w), coordconverter(ao12y, pygame.display.Info().current_w)))
    if currtime > 60000:
        min = int(currtime / 60000)
        sec = ((currtime - min * 60000) / 1000)
        screen.blit(gamefont(coordconverter(60, pygame.display.Info().current_w)).render(f"{(min)}:{(sec):0.3f}", True, color), (coordconverter(900, pygame.display.Info().current_w), coordconverter(500, pygame.display.Info().current_w)))
    else:
        screen.blit(gamefont(coordconverter(60, pygame.display.Info().current_w)).render(f"{(currtime/1000):0.3f}", True, color), (coordconverter(900, pygame.display.Info().current_w), coordconverter(500, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render(first_ten_moves, True, BLACK), (coordconverter(850, pygame.display.Info().current_w), coordconverter(400, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render(last_ten_moves, True, BLACK), (coordconverter(800, pygame.display.Info().current_w), coordconverter(450, pygame.display.Info().current_w)))
    if virtual_solving:
        screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render("Virtual solving (\\ to toggle)", True, GREEN), (coordconverter(800, pygame.display.Info().current_w), coordconverter(800, pygame.display.Info().current_w)))
    else:
        screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render("Virtual solving (\\ to toggle)", True, RED), (coordconverter(800, pygame.display.Info().current_w), coordconverter(800, pygame.display.Info().current_w)))

print(genscramble())