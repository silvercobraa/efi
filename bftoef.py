#!/usr/bin/env python
# coding=utf-8

import sys

mapping = {
    '>': '😂', # Move pointer one cell to the left
    '<': '👌', # Move pointer one cell to the right
    '+': '💦', # Increment value of the cell curently pointed
    '-': '💯', # Decrement value of the cell currently pointed
    ',': '🔥', # read character from standard input to the cell
    '.': '😭', # write value to standard output
    '[': '🍆', # begin for
    ']': '✔', # end for
}

with open(sys.argv[1]) as f:
    ch = f.read(1)
    while ch != '':
        try:
            print(mapping[ch], end='')
        except KeyError as ke:
            pass
        ch = f.read(1)
