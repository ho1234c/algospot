import sys
rl = lambda: sys.stdin.readline()
n = int(rl())
varDict = {
    'zero': 0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,
}


def checkString(str):
    strSort = list(str)
    strSort.sort()
    strSort = "".join(strSort)
    for i in varDict:
        temp = list(i)
        temp.sort()
        temp = "".join(temp)
        if len(strSort) == len(temp) and checkList(strSort, temp): return i
    return False


def checkList(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]: return False
    return True


for i in range(n):
    problem = rl().strip().split('=')
    for j in varDict.keys():
        problem[0] = problem[0].replace(j, str(varDict.get(j)))
    answer = varDict.get(checkString(problem[1].strip()))
    result = eval(problem[0].strip()) == answer and 'Yes' or 'No'
    print result