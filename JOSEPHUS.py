import sys
rl = lambda: sys.stdin.readline()
input = rl().strip().split(" ")

roundTable = range(1, int(input[0])+1)
jumpVal = int(input[1])

pointer = 0

satisfaction = 0

result = []

while roundTable:
    satisfaction += 1

    if satisfaction == jumpVal:
        result.append(roundTable.pop(pointer))
        satisfaction = 0
    else:
        pointer += 1

    if pointer >= len(roundTable):
        pointer -= len(roundTable)

output = str(result)[1:-1]

print '<' + output + '>'
