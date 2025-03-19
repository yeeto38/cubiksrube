import os
import tkinter as tk
import pygame
import numpy as np
import csv
from cubetimer import *
from dasinput import *
from algcalc import *
from practice import *
from universal import *
from menu import *

# -------- Functions -----------

def csvwriter(time, scramble):
    with open ('times.csv', 'a+') as csvfile:
        csvwriting = csv.writer(csvfile)
        csvwriting.writerow([time, scramble])

# -------- Main Program Loop -----------

def main():
    lastpress = 0
    # amount of ms before key can be pressed again. can be customized
    das = 100
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
    # Use tkinter to get the screen length and width
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    def get_screen_size(root):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        return screen_width, screen_height

    screen_width, screen_height = get_screen_size(root)
    size = (int(0.8 *screen_width), int(0.8*screen_height))
    # The size of the new screen from tkinter
    newscreen = size[0]

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
    if not os.path.exists('times.csv'):
        with open('times.csv', 'w') as csvfile:
            csv.writer(csvfile)
    with open('times.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            prevsolves = np.roll(prevsolves, 1)
            prevsolves[0] = float(row[0])

    # Set the width and height of the screen [width, height]
    # leng = open_popup()

    # size = (leng, int(leng * 9 / 14))

    screen = pygame.display.set_mode(size)
    
    # Initialize pygame
    pygame.init()

    keymapimg = pygame.image.load(resource_path("Cubiks_Rube/keymap.png"))
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

        if currevent == 0:
            drawmenu(screen, hover)
        elif currevent == 1:
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
        elif currevent == 4:
            drawcube(screen, cube)
            algbox(screen, invalidnotation, useralg)
            algcalc_words(screen, analysis)
        permtext(screen)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # print(newscreen)
        # --- Limit to 60 frames per second
        clock.tick(60)
    # Close the window and quit.
    pygame.quit()

if __name__ == "__main__":
    main()