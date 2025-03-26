# This file contains functions that are used in multiple files in the program.

import os
import sys
import pygame

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def coordconverter(num, screenw):
    return num / 1400 * screenw

def get_screen_size(root):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        return screen_width, screen_height

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

# Draws the keymap
def drawkeymap(screen, size, keymapimg):
    # takes in the size of the screen
    keymapsize = keymapimg.get_size()
    newimg = pygame.transform.scale(keymapimg, (coordconverter(keymapsize[0], size[0]), coordconverter(keymapsize[1], size[0])))
    newimgsize = newimg.get_size()
    screen.blit(newimg, ((size[0] - newimgsize[0])/2, (size[1] - newimgsize[1])/2))
    return