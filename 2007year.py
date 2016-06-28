import sys
rl = lambda: sys.stdin.readline()
input  = str(rl().strip()).split(" ")

# input value
inputMonth = int(input[0])
inputDay = int(input[1])

# init about the day
lastDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

dayCount = inputDay
for i in range(0, inputMonth-1):
    dayCount += lastDay[i]

print week[dayCount % 7]
