# https://parclytaxel.tumblr.com/post/87085714319/interpreter-for-1-in-python

#!/usr/bin/env python
# 1+ interpreter in Python
# Parcly Taxel / Jeremy Tan, 2014
# Licence is CC BY-SA 4.0 / FAL 1.3 / GNU GPLv3
import sys
from collections import deque

s, sd = deque(), {}

def oneplus(raw = ""):
    hm, R, bst, B, N = [], {}, deque(), 0, 0
    program_output = ""
    for c in raw:
        if c == '(':
            B += 1
            bst.append(N)
        if c == ')':
            B -= 1
            R[bst.pop()] = N
            if B < 0:
                return 2
        if c == '#' and B == 0: hm.append(N)
        N += 1
    if B != 0:
        return 2
    
    N, cmt = 0, False
    cnt = 0
    while N < len(raw) and cnt <= 500:
        op = raw[N]
        if not cmt:
            if op == '1': s.append(1)
            elif op == '+': s.append(s.pop() + s.pop())
            elif op == '*': s.append(s.pop() * s.pop())
            elif op == '"': s.append(s[-1])
            elif op == '/': s.rotate(1)
            elif op == '\\': s.rotate(-1)
            elif op == '^': s.extend([s.pop(), s.pop()])
            elif op == '<': s.append(0 if s.pop() < s.pop() else 1)
            elif op == '#': N = hm[s.pop()]
            elif op == '.': s.append(abs(int(raw_input('number: '))))
            elif op == ',': s.append(ord(raw_input('character: ')[0]))
            elif op == ':': program_output += str(s.pop())
            elif op == ';': sys.stdout.write(unichr(s.pop()))
            elif op == '[': cmt = True
            elif op == '(':
                rtn = raw[N + 1:R[N]].partition('|')
                if rtn[1]: sd[rtn[0]] = rtn[2]
                oneplus(sd[rtn[0]])
                N = R[N]
            elif op == 'd' : print s
        else:
            if op == ']': cmt = False
        N += 1
        cnt += 1
    if cnt == 501:
        return 3
    return program_output
if __name__ == "__main__":
    oneplus('11##":1+1#')
