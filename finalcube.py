import os
import sys
import tkinter as tk
from tkinter import messagebox
import pygame
import random
import math
import numpy as np
import csv
from rotations import (
    rotateSP, rotateE, rotatef, rotateb, rotateM, rotatebp, rotatefp, rotateEP, rotateS, rotateZP, rotateB, rotateLP, rotatelp, rotateX, rotater, rotateR, rotateBP, rotateZ, rotateYP, rotateD, rotateL, rotateUP, rotateFP, rotateF, rotateU, rotateRP, rotateDP, rotateY, rotated, rotateMP, rotateup, rotatel, rotateXP, rotaterp, rotateu, rotatedp, rotateF2, rotateR2, rotateD2, rotateL2, rotateU2, rotateB2, rotateM2, rotateE2, rotateS2, rotateX2, rotateY2, rotateZ2, rotatef2, rotateb2, rotateu2, rotated2, rotater2, rotatel2
)

leng = 1200

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def defstate() :
    cube = np.zeros((6, 3, 3), dtype=object)
    for i in range(6):
        for j in range(3):
            for k in range(3):
                cube[i][j][k] = colors()[i]
    return cube

#YRGOWB
def colors():
    return [YELLOW, RED, GREEN, ORANGE, WHITE, BLUE]

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
def gamefont(size):
    return pygame.font.Font(resource_path("Ubuntu-B.ttf"), int(size))
    # return pygame.freetype.SysFont("ヒラキノ角コシックw9", coordconverter(48, pygame.display.Info().current_w))
def algfont():
    return pygame.font.Font(resource_path("UbuntuMono-R.ttf"), int(coordconverter(20, pygame.display.Info().current_w)))

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
    return

def menu_options():
    return ["(p)ractice", "(c)hange das", "(t)imer", "(a)lg calculator", "(q)uit program"]

# keymap actions
key_actions = {
    pygame.K_1: rotateSP, pygame.K_2: rotateE, pygame.K_3: rotatef, pygame.K_4: rotateb, pygame.K_5: rotateM, pygame.K_6: rotateM,
    pygame.K_7: rotatebp, pygame.K_8: rotatefp, pygame.K_9: rotateEP, pygame.K_0: rotateS, pygame.K_q: rotateZP, pygame.K_w: rotateB,
    pygame.K_e: rotateLP, pygame.K_r: rotatelp, pygame.K_t: rotateX, pygame.K_y: rotateX, pygame.K_u: rotater, pygame.K_i: rotateR,
    pygame.K_o: rotateBP, pygame.K_p: rotateZ, pygame.K_a: rotateYP, pygame.K_s: rotateD, pygame.K_d: rotateL, pygame.K_f: rotateUP,
    pygame.K_g: rotateFP, pygame.K_h: rotateF, pygame.K_j: rotateU, pygame.K_k: rotateRP, pygame.K_l: rotateDP, pygame.K_SEMICOLON: rotateY,
    pygame.K_z: rotated, pygame.K_x: rotateMP, pygame.K_c: rotateup, pygame.K_v: rotatel, pygame.K_b: rotateXP, pygame.K_n: rotateXP,
    pygame.K_m: rotaterp, pygame.K_COMMA: rotateu, pygame.K_PERIOD: rotateMP, pygame.K_SLASH: rotatedp,
}

# text actions
def text_to_action():
    return {
    "F": rotateF, "Fp": rotateFP, "F2": rotateF2, "R": rotateR, "Rp": rotateRP, "R2": rotateR2, "D": rotateD, "Dp": rotateDP, "D2": rotateD2,
    "L": rotateL, "Lp": rotateLP, "L2": rotateL2, "U": rotateU, "Up": rotateUP, "U2": rotateU2, "B": rotateB, "Bp": rotateBP, "B2": rotateB2,
    "M": rotateM, "Mp": rotateMP, "M2": rotateM2, "E": rotateE, "Ep": rotateEP, "E2": rotateE2, "S": rotateS, "Sp": rotateSP, "S2": rotateS2,
    "x": rotateX, "xp": rotateXP, "x2": rotateX2, "y": rotateY, "yp": rotateYP, "y2": rotateY2, "z": rotateZ, "zp": rotateZP, "z2": rotateZ2,
    "f": rotatef, "fp": rotatefp, "f2": rotatef2, "b": rotateb, "bp": rotatebp, "b2": rotateb2, "u": rotateu, "up": rotateup, "u2": rotateu2,
    "d": rotated, "dp": rotatedp, "d2": rotated2, "r": rotater, "rp": rotaterp, "r2": rotater2, "l": rotatel, "lp": rotatelp, "l2": rotatel2,
    "m": rotateM, "mp": rotateMP, "m2": rotateM2, "e": rotateE, "ep": rotateEP, "e2": rotateE2, "s": rotateS, "sp": rotateSP, "s2": rotateS2,
    "X": rotateX, "Xp": rotateXP, "X2": rotateX2, "Y": rotateY, "Yp": rotateYP, "Y2": rotateY2, "Z": rotateZ, "Zp": rotateZP, "Z2": rotateZ2
    }   

# -------- Functions -----------

# Splits a string of moves into a list of moves that can be used by virtual cube program
def splitmoves(move_string):
    moves = move_string.split(" ")
    out = []
    for move in moves:
        if len(move) == 1:
            out.append(move)
        elif move[1] in ["p", "P", "'"]:
            out.append(move[0] + "p")
        else:
            out.append(move[0] + "2")
    if out[0].lower() in ["x", "y", "z"]:
        out[0] == out[0].lower()
    elif out[0].lower() in ["s", "e", "m"]:
        out[0] == out[0].upper()
    return out

# Checks if a move is a valid move
def is_valid_move(moves):
    for move in moves:
        if move not in text_to_action():
            return False
    return True

# Converts a move to an action
def move_to_action(move):
    return text_to_action()[move]
# Draws the keymap
def drawkeymap(screen, size, keymapimg):
    # takes in the size of the screen
    keymapsize = keymapimg.get_size()
    newimg = pygame.transform.scale(keymapimg, (coordconverter(keymapsize[0], size[0]), coordconverter(keymapsize[1], size[0])))
    newimgsize = newimg.get_size()
    screen.blit(newimg, ((size[0] - newimgsize[0])/2, (size[1] - newimgsize[1])/2))
    return
# Draw the menu
def drawmenu(screen, hover):
    screen.blit(gamefont(coordconverter(60, pygame.display.Info().current_w)).render("MENU", True, BLACK), (coordconverter(600, pygame.display.Info().current_w), coordconverter(250, pygame.display.Info().current_w)))
    for i in range(len(menu_options())):
        color = RED if i == hover else BLACK
        screen.blit(gamefont(coordconverter(30, pygame.display.Info().current_w)).render(menu_options()[i], True, color), (coordconverter(600, pygame.display.Info().current_w), coordconverter(350, pygame.display.Info().current_w) + (i * coordconverter(40, pygame.display.Info().current_w))))

# Write the permanent text
def permtext(screen):
    screen.blit(gamefont(coordconverter(48, pygame.display.Info().current_w)).render("Rubik's Cube", True, BLACK), (coordconverter(20, pygame.display.Info().current_w), coordconverter(20, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(48, pygame.display.Info().current_w)).render("Utility", True, BLACK), (coordconverter(20, pygame.display.Info().current_w), coordconverter(72, pygame.display.Info().current_w)))
    screen.blit(gamefont(coordconverter(26, pygame.display.Info().current_w)).render("menu (=)", True, BLACK), (coordconverter(20, pygame.display.Info().current_w), coordconverter(140, pygame.display.Info().current_w)))

# Practice stuff
def practice_words(screen):
    screen.blit(gamefont(coordconverter(20, pygame.display.Info().current_w)).render("(esc) to reset cube", True, BLACK), (coordconverter(1150, pygame.display.Info().current_w), coordconverter(30, pygame.display.Info().current_w)))

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

# Keybinds Words Renderer
def keybinds_words(screen):
    # Render the keybinds text on the screen.
    screen.blit(gamefont(coordconverter(26, pygame.display.Info().current_w)).render("keybinds (-)", True, BLACK), (coordconverter(20, pygame.display.Info().current_w), coordconverter(190, pygame.display.Info().current_w)))

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
    screen.blit(pygame.font.Font(resource_path("UbuntuMono-R.ttf"), int(coordconverter(20, pygame.display.Info().current_w))).render(useralg, True, BLACK, None), (input_rectalg.x+coordconverter(5, pygame.display.Info().current_w), input_rectalg.y+coordconverter(3, pygame.display.Info().current_w)))
    # Display error message if the algorithm notation is invalid

def solved(cube):
    # Iterate through all cube faces to check if each face is a solid color
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if cube[i][j][k] != cube[i][1][1]:
                    return False
    return True

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

def scramb(scramble):
    moves = splitmoves(" ".join(scramble))
    cube = defstate()
    for move in moves:
        move_to_action(move)(cube)
    return cube

def coordconverter(num, screen0):
    return num / 1400 * screen0

def csvwriter(time, scramble):
    with open ('times.csv', 'a+') as csvfile:
        csvwriting = csv.writer(csvfile)
        csvwriting.writerow([time, scramble])

def genscramble():
    smoves = ["R", "U", "F", "L", "D", "B", "R'", "U'", "F'", "L'", "D'", "B'", "R2", "U2", "F2", "L2", "D2", "B2"]
    out = []
    prev = 0
    curr = 0
    # Generate 20 random moves
    for _ in range(20):
        # Make sure the next move is not the same as the previous
        curr = random.randint(0, len(smoves)-1)
        while curr % 6 == prev % 6:
            curr = random.randint(0, len(smoves) - 1)
        out.append(smoves[curr])
        prev = curr % 6
    return out

def open_popup():
    """Opens a pop-up window to prompt the user to enter an integer number."""
    result = [None]  # Use a list to store the result

    def submit_number():
        try:
            number = int(entry.get())
            result[0] = number
        except ValueError or NameError:
            messagebox.showerror("Invalid Input", "Size set to default (1200px).")
            result[0] = 1200
        popup.destroy()

    popup = tk.Tk()  # Create the pop-up window as the main window
    popup.title("Screen size selection")
    popup.focus_force()  # Focus the window
    label = tk.Label(popup, text="Please enter the px value for width of screen:")
    label.pack(padx=20, pady=10)
    entry = tk.Entry(popup)
    entry.pack(padx=20, pady=10)
    entry.focus_set()  # Set focus to the entry widget
    entry.bind("<Return>", lambda event: submit_number())  # Bind Enter key to submit_number
    submit_button = tk.Button(popup, text="Submit", command=submit_number)
    submit_button.pack(pady=10)
    popup.mainloop()

    return result[0]

# -------- Main Program Loop -----------

def main():

    lastpress = 0
    # amount of ms before key can be pressed again. can be customized
    das = 120
    # das for the menu. cannot be customized outside of code
    menudas = 150
    #0 = menu
    #1 = virtual cube (nothing more)
    #2 = changing das
    #3 = timer (with scramble) 
    #   have option to include analytics, such as tps, average, etc.
    #4 = count alg time (display overloading?)
    currevent = 0
    prevevent = 1
    userdas = ''
    hover = 0
    # the keymap and moveset for the cube
    moves = np.array(["S'", "E", "f", "b", "M", "M", "b'", "f'", "E'", "S", "z'", "B", "L'", "l'", "x", "x", "r", "R", "B'", "z", "y'", "D", "L", "U'", "F'", "F", "U", "R'", "D'", "y", "d", "M'", "u'", "l", "x'", "x'", "r'", "u", "M'", "d'"])
    times = np.zeros(len(moves))

    drawkeys = False
    invalidnum = False
    useralg = ''
    invalidnotation = False
    # Loop until the user clicks the close button
    # pygame.K_RETURN works VERY well
    done = False
    acceptable_inputs = [pygame.K_r, pygame.K_u, pygame.K_f, pygame.K_l, pygame.K_d, pygame.K_b, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_m, pygame.K_e, pygame.K_s, pygame.K_SPACE, pygame.KSCAN_APOSTROPHE, pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_p, pygame.K_BACKSLASH, pygame.K_ESCAPE, pygame.K_2]

    #timer variables
    prevsolves = np.zeros(12, dtype=float)
    spaceholdstart = 0
    timer_start = 0
    timing = False
    currtime = 0
    timercolor = None
    scramble = []
    virtual_solving = False
    analysis = [0, 0, 0, 0, 0, 0]

    # Use to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Check if times.csv exists, if not create it with headers
    try:
        with open('times.csv', 'x') as csvfile:
            csv.writer(csvfile)
    except FileExistsError:
        pass
    with open('times.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') 
        for row in reader:
            prevsolves = np.roll(prevsolves, 1)
            prevsolves[0] = float(row[0])

    # Set the width and height of the screen [width, height]
    leng = open_popup()

    size = (leng, int(leng * 9 / 14))

    screen = pygame.display.set_mode(size)
    
    # Initialize pygame
    pygame.init()

    keymapimg = pygame.image.load(resource_path("keymap.png"))
    # sets alpha to 128
    keymapimg.set_alpha(128)

    scramble = genscramble()

    cube = defstate()
    for i in range(6):
        for j in range(3):
            for k in range(3):
                    cube[i][j][k] = colors()[i]

    while not done:
        # Clear the screen to white before drawing anything new
        screen.fill(WHITE)

        # --- Main event loop
        for event in pygame.event.get():
            # Handle quit events
            if event.type == pygame.QUIT:
                done = True

            # Detect key presses for universal actions
            keys = pygame.key.get_pressed()

            # Main Menu Actions
            if currevent == 0:
                if keys[pygame.K_ESCAPE]:
                    currevent = prevevent
                    lastpress = pygame.time.get_ticks()
                # Navigate menu options using keys
                if keys[pygame.K_c]:
                    if pygame.time.get_ticks() - lastpress > menudas:
                        lastpress = pygame.time.get_ticks()
                        currevent = 2
                        userdas = str(das)
                if keys[pygame.K_p]:
                    if pygame.time.get_ticks() - lastpress > menudas:
                        lastpress = pygame.time.get_ticks()
                        currevent = 1
                        cube = defstate()
                if keys[pygame.K_t]:
                    if pygame.time.get_ticks() - lastpress > menudas:
                        scramble = genscramble()
                        cube = scramb(scramble)
                        lastpress = pygame.time.get_ticks()
                        currevent = 3
                if keys[pygame.K_a]:
                    if pygame.time.get_ticks() - lastpress > menudas:
                        lastpress = pygame.time.get_ticks()
                        currevent = 4
                if keys[pygame.K_q]:
                    done = True
                if keys[pygame.K_UP]:
                    if hover > 0:
                        hover -= 1
                    else:
                        hover = len((menu_options())) - 1
                if keys[pygame.K_DOWN]:
                    if hover < len(menu_options()) - 1:
                        hover += 1
                    else:
                        hover = 0
                if keys[pygame.K_RETURN]:
                    currevent = hover + 1
                    lastpress = pygame.time.get_ticks()
                    # Handle specific menu options
                    if hover == 0:
                        cube = defstate()
                    elif hover == 1:
                        userdas = str(das)
                    elif hover == 2:
                        cube = defstate()
                    elif hover == 3:
                        scramble = genscramble()
                        cube = scramb(scramble)
                        prevsolves = np.zeros(5, dtype=float)
                        currtime = 0
                        timing = False
                        timer_start = 0
                        spaceholdstart = 0
                        virtual_solving = False
                    elif hover == 4:
                        done = True

            # Handle Virtual Cube (currevent == 1)
            elif currevent == 1:
                # Toggle keybind visibility
                if keys[pygame.K_MINUS]:
                    if pygame.time.get_ticks() - lastpress > menudas:
                        lastpress = pygame.time.get_ticks()
                        drawkeys = not drawkeys

                # Perform cube actions based on key presses
                for key, action in key_actions.items():
                    if keys[key]:
                        index = list(key_actions.keys()).index(key)
                        if pygame.time.get_ticks() - times[index] > das:
                            times[index] = pygame.time.get_ticks()
                            cube = action(cube)
                    if keys[pygame.K_ESCAPE]:
                        if pygame.time.get_ticks() - lastpress > menudas:
                            lastpress = pygame.time.get_ticks()
                            cube = defstate()
            # changing das actions
            elif currevent == 2:
                if pygame.time.get_ticks() - lastpress > menudas:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if userdas != '':
                                das = int(userdas)
                                currevent = 0
                            currevent = 0
                        elif event.key == pygame.K_BACKSPACE:
                            userdas = userdas[:-1]
                        else:
                            # if event.unicode.isdigit():
                            #     userdas += event.unicode
                            #     invalidnum = False
                            # else:
                            #     invalidnum = True
                            if len(userdas) < 3:
                                if event.unicode.isdigit():
                                    userdas += event.unicode
                                    invalidnum = False
                            else:
                                invalidnum = True
            # timer actions
            elif currevent == 3:
                # keybinds
                if keys[pygame.K_MINUS]:
                    if pygame.time.get_ticks() - lastpress > menudas:
                        lastpress = pygame.time.get_ticks()
                        drawkeys = not drawkeys

                # cube actions
                if timing and virtual_solving:
                    for key, action in key_actions.items():
                        if keys[key]:
                            index = list(key_actions.keys()).index(key)
                            if pygame.time.get_ticks() - times[index] > das:
                                times[index] = pygame.time.get_ticks()
                                cube = action(cube)
                    if solved(cube):
                        lastpress = pygame.time.get_ticks()
                        timing = False
                        timercolor = BLACK
                        prevsolves = np.roll(prevsolves, 1)
                        prevsolves[0] = currtime
                        csvwriter(currtime, scramble)
                        spaceholdstart = 0
                        timer_start = 0
                        scramble = genscramble()
                        cube = scramb(scramble)

                # toggles virtual solving
                if keys[pygame.K_BACKSLASH] and not timing:
                    if pygame.time.get_ticks() - lastpress > 100:
                        virtual_solving = not virtual_solving
                        lastpress = pygame.time.get_ticks()

                # when space is pressed
                if keys[pygame.K_SPACE]:
                    if spaceholdstart == 0:
                        spaceholdstart = pygame.time.get_ticks()
                    elapsed = pygame.time.get_ticks() - spaceholdstart
                    timercolor = GREEN if elapsed > 1000 else RED
                    if timing:
                        if not virtual_solving:
                            if pygame.time.get_ticks() - lastpress > 100:
                                lastpress = pygame.time.get_ticks()
                                timing = False
                                timercolor = BLACK
                                prevsolves = np.roll(prevsolves, 1)
                                prevsolves[0] = currtime
                                csvwriter(currtime, scramble)
                                spaceholdstart = 0
                                timer_start = 0
                                scramble = genscramble()
                                cube = scramb(scramble)
                else:
                    timercolor = BLACK
                    if spaceholdstart != 0:
                        if elapsed > 1000 and not timing:
                            timing = True
                            timer_start = pygame.time.get_ticks()
                        spaceholdstart = 0

                # resets timer when esc pressed
                if keys[pygame.K_ESCAPE] or keys[pygame.K_EQUALS]:
                    currtime = 0
                    timing = False
                    timer_start = 0
                    spaceholdstart = 0

            elif currevent == 4:
                if pygame.time.get_ticks() - lastpress > menudas:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if useralg != '':
                                try:
                                    moves = splitmoves(useralg)
                                    for move in moves:
                                        move_to_action(move)(cube)
                                        drawcube(screen, cube)
                                        lastpress = pygame.time.get_ticks()
                                    else:
                                        invalidnotation = False
                                    analysis = move_analyzer(moves)
                                except:
                                    invalidnotation = True
                            else:
                                invalidnotation = True
                        elif event.key == pygame.K_BACKSPACE:
                            useralg = useralg[:-1]
                        else:
                            if event.key in acceptable_inputs:
                                if event.key == pygame.K_ESCAPE:
                                    currevent = 0
                                elif event.key == pygame.K_BACKSLASH:
                                    cube = defstate()
                                else:
                                    if event.unicode == "P" or event.unicode == "p":
                                        useralg += "'"
                                    else:
                                        useralg += event.unicode
                                    invalidnotation = False
                            else:
                                invalidnotation = True

            if keys[pygame.K_EQUALS]:
                if pygame.time.get_ticks() - lastpress > menudas:
                    lastpress = pygame.time.get_ticks()
                    # Hide keybinds or return to menu from other events
                    if currevent == 1 or currevent == 3 or currevent == 4:
                        drawkeys = False
                        prevevent = currevent
                        currevent = 0

        if currevent == 1:
            drawcube(screen, cube)
            if drawkeys:
                drawkeymap(screen, size, keymapimg)
            keybinds_words(screen)
            practice_words(screen)
        elif currevent == 2:
            drawdasbox(screen, invalidnum, userdas)
        elif currevent == 3:
            if timing:
                currtime = pygame.time.get_ticks() - timer_start
            drawcube(screen, cube)
            if drawkeys:
                drawkeymap(screen, size, keymapimg)
            timer_words(screen, prevsolves, currtime, timercolor, scramble, virtual_solving)
            keybinds_words(screen)
        elif currevent == 0:
            drawmenu(screen, hover)
        elif currevent == 4:
            drawcube(screen, cube)
            algbox(screen, invalidnotation, useralg)
            algcalc_words(screen, analysis)

        permtext(screen)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 1 frames per second
        # clock.tick(60)

    # Close the window and quit.
    pygame.quit()

if __name__ == "__main__":
    main()