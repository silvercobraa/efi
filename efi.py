#!/usr/bin/env python
# coding=utf-8
# EmojiFuck Interpreter (version 0)
# author: César Bolívar Severino

import sys

TAPE_SIZE = 30000

MOVL = '😂'
MOVR = '👌'
INCC = '💦'
DECC = '💯'
GETC = '🔥'
PUTC = '😭'
BFOR = '🍆'
EFOR = '✔'

def interpret(program, tape):
    ptr = 0;
    current_char = program.read(1)
    stack = []
    # while current_char != '':
    while current_char != '':
        # print(current_char)
        if current_char == MOVR:
            ptr += 1;
        elif current_char == MOVL:
            ptr -= 1;
        elif current_char == INCC:
            tape[ptr] += 1;
        elif current_char == DECC:
            tape[ptr] -= 1;
        elif current_char == PUTC:
            print(chr(tape[ptr]), end='')
        elif current_char == GETC:
            ch = sys.stdin.read(1)
            # print(ch)
            tape[ptr] = ord(ch)
        elif current_char == BFOR:
            if tape[ptr] != 0:
                stack.append(program.tell())
            else:
                balance = 1
                while balance != 0:
                    current_char = program.read(1)
                    if current_char == BFOR:
                        balance += 1
                    elif current_char == EFOR:
                        balance -= 1
        elif current_char == EFOR:
            if tape[ptr] != 0:
                program.seek(stack[-1], 0)
            else:
                stack.pop()
        current_char = program.read(1)


if len(sys.argv) < 2:
    print('python efi.py example.ef')
    sys.exit(1)

with open(sys.argv[1], 'r') as source:
    tape = [0 for i in range(TAPE_SIZE)]
    interpret(source, tape)
