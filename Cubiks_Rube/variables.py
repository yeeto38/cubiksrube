# This file contains all the constant variables used in the program

import numpy as np
import pygame
from universal import resource_path, coordconverter
from rotations import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

def defstate():
    cube = np.zeros((6, 3, 3), dtype=object)
    for i in range(6):
        for j in range(3):
            for k in range(3):
                cube[i][j][k] = colors()[i]
    return cube

#YRGOWB
def colors():
    return [YELLOW, RED, GREEN, ORANGE, WHITE, BLUE]

def gamefont(size):
    return pygame.font.Font(resource_path("Cubiks_Rube/Ubuntu-B.ttf"), int(size))

def algfont():
    return pygame.font.Font(resource_path("Cubiks_Rube/UbuntuMono-R.ttf"), int(coordconverter(20, pygame.display.Info().current_w)))

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

# Converts a move to an action
def move_to_action(move):
    return text_to_action()[move]