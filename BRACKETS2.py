import sys
rl = lambda: sys.stdin.readline()
n = int(rl())

for i in range(n):
    inputStr = rl()
    openBrk = ['(', '{', '[']
    closeBrk = [')', '}', ']']
    stack = []
    result = 'YES'
    for j in list(inputStr):
        if j in openBrk:
            stack.append(j)
        elif j in closeBrk:
            if not len(stack):
                result = 'NO'
                break
            for x, y in zip(openBrk, closeBrk):
                if j == y:
                    if x == stack[len(stack)-1]:
                        stack.pop()
                    else:
                        result = 'NO'
                        break
    if len(stack):
        result = 'NO'
    print result