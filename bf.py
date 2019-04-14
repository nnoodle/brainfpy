#!/usr/bin/env python3
# "fascist", score-computing interpreter (http://www.hevanet.com/cristofd/brainfuck)
import sys

with open(sys.argv[1], "r") as src:
    rom = ''.join(src.readlines())

# rom = """
# >++++++++[-<+++++++++>]<.>>+>-[+]++>++>+++[>[->+++<<+++>]<<]>-----.>->
# +++..+++.>-.<<+[>[+>+]>>]<--------------.>>.+++.------.--------.>+.>+.
# """

jmp = 0
pairs = 0
ptr = 0
rptr = 0
tape = [0]

def skip(fro, to, mod):
    global jmp, pairs, rptr
    rptr += mod
    if rom[rptr] == fro:
        pairs += 1
    elif rom[rptr] == to:
        if pairs != 0:
            pairs -= 1
        else:
            jmp = 0

while rptr < len(rom):
    # print("#", ptr, rom[rptr], rptr, jmp, pairs, tape)
    if jmp == 1:
        skip('[', ']', 1)
    elif jmp == -1:
        skip(']', '[', -1)
    elif rom[rptr] == '[' and tape[ptr] == 0:
        jmp = 1
    elif rom[rptr] == ']' and tape[ptr] != 0:
        jmp = -1
    else:
        if rom[rptr] == '.':
            print(chr(tape[ptr]), end='')
        elif rom[rptr] == ',':
            tape[ptr] = ord(sys.read(1))
        elif rom[rptr] == '+':
            tape[ptr] += 1
        elif rom[rptr] == '-':
            tape[ptr] -= 1
        elif rom[rptr] == '>':
            ptr += 1
        elif rom[rptr] == '<':
            ptr -= 1
        rptr += 1
    if (ptr+2) > len(tape):
        tape = (tape + (ptr+1) * [0])[:(ptr+1)]
