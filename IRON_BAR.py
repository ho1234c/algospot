# -*- coding: utf-8 -*-
import sys
rl = lambda: sys.stdin.readline()
inputStr = list(rl().strip())

result = 0
height = 0

for i in range(0, len(inputStr)):
    if inputStr[i] == '(':
        height += 1

    elif inputStr[i] == ')':
        height -= 1

        if inputStr[i-1] == '(':
            result += height
        else:
            result += 1

print result

# 레이저가 나타났을 때 추가되는 쇠막대기의 수 = 이전 레이저 사이의 ')'의 갯수 + 시작부터 지금까지 아직 열려있는 '('의 갯수
