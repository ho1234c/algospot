# -*- coding: utf-8 -*-
import sys
rl = lambda: sys.stdin.readline()
n = int(rl())
count = 0

def safeCheck(n, pos, field):
    return not any(t in (n, n - i, n + i) for t, i in zip(field, range(pos, 0, -1)))


def search(field, pos, fieldSize):
    if pos == fieldSize:
        global count
        count = count +1
        return None

    for n in range(fieldSize):
        if safeCheck(n, pos, field):
            field[pos] = n
            search(field, pos+1, fieldSize)

for repeat in range(n):
    fieldSize = int(rl())
    chessField = [0] * fieldSize
    search(chessField, 0, fieldSize)
    print count

# N queen probrlem 시간초과, 모르겠음

