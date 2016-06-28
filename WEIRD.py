import sys, math
from itertools import combinations

rl = lambda: sys.stdin.readline()
n = int(rl())
num = []

for i in range(n):
    targetNum = int(rl())
    divSet = []
    result = False
    for n in xrange(1, int(math.sqrt(targetNum))+1):
        if targetNum % n == 0:
            divSet.append(n)
            if n * n != targetNum:
                divSet.append(targetNum/n)
    divSet.remove(targetNum)
    if sum(divSet) <= targetNum:
        result = True
    else:
        for k in xrange(3, len(divSet)+1):
            for j in combinations(divSet, k):
                if sum(j) == targetNum:
                    result = True
                    break
            if result: break
    result = result and 'not weird' or 'weird'
    print result

