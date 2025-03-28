## cubiksrube
Rubik's Cube project

Keybinds are pretty self expalanatory, (-) key to show keybinds for practice.

The Alg calculator function is kinda just there for fun, tried to make it off of Jperm's Your Algorithm Sucks (proof) video

When it says pip install, it might be python3 -m pip or python -m pip. It depends on how you downloaded python

To run:
- If you don't have python installed already, do that (https://www.python.org)
- In your terminal, cd to the directory you downloaded the this file to (ie. cd Downloads/cubiksrube) 
    - type vim ~/.bash_profile
        - press 'o' and then type 'alias python='python3.13'
        - press 'esc' then press ':wq'
    - type 'pip install .'
    - You can now just run finalcube.py and it should work just fine
    - You can also run it as an exe 
        - If you are on mac:
            - type 'pip install ."[extra]"'
        - If you are on windows:
            - type 'pip install .[extra]
        - type pyinstaller cubiksrube.spec
            - This may take a while and there will be a bunch of numbers and letters going on your terminal. This is fine.
        - Go to finder/file explorer and in ./cubiksrube/dist there should be an executable file
        - Double click to run. A terminal will open and you just have to wait a bit for the program to open
