# -*- coding: utf-8 -*-
import sys
rl = lambda: sys.stdin.readline()
n = int(rl())


def change(goal, cointype, count, pos, result):
    while pos >= 0:
        while True:
            count[pos] += 1
            if multiply(cointype, count) == goal:
                result += 1
                return result

            return change(goal, cointype, count, pos-1, result)
        pos -= 1


def calc(start, goal, unit):
    current = start
    while goal > current:
        current += unit
    return goal - current


def multiply(list1, list2):
    result = 0
    for a, b in zip(list1, list2):
        result += a * b
    return result

for i in range(n):
    inputStr = rl().split()
    inputCoin = rl().split()
    count = 0
    target = {
        'price': [int(inputStr[0])],
        'num': int(inputStr[1]),
        'coin': [a for a in map(int, inputCoin) if a <= int(inputStr[0])]
    }
    target['coin'].sort()

    print 2**64
    print 1000000007**2
    # print change(110, [100,50,10])

    # while True:
    #     for k in set(target['price']):
    #         if change(k, target['coin'], []):   # 쪼갤 수 있는가?
    #             count += 1
    #
    #     for y in target['price']:
    #         temp = change(y, target['coin'], [])
    #         if len(temp) > 1:
    #                 target['price'].extend(temp)  # 리스트중 하나만 쪼개진 값으로 대체
    #                 target['price'].remove(y)
    #                 break
    #     else:
    #         break
    #
    #     print(target['price'])

    print count

# 가장 적게 거스름돈을 줄 수 있는 방법(greedy algorithm)을 선택한 후 쪼개나간다.
# 쪼개는 것은 대체될수 있음을 뜻함. 따라서 경우의수 증가
# [10, 50, 100, 500] target 보다 큰 값 제거
# [10, 50, 100] 정렬한 후 가장 큰 단위부터 쪼개나감
# [10, 50, [50, 50]]
# [10, 50, [[10,10,10,10,10], [10,10,10,10,10]]]
# [10, [10,10,10,10,10], [[10,10,10,10,10], [10,10,10,10,10]]]
#
# 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
# [50, 10, 10, 10, 10, 10, 10],
# [50, 50, 10]
# [100, 10]
# [110]

# 1
# 110 4
# 10 50 100 500
