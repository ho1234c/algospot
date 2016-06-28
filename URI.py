import sys
import urllib2
rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    str = rl().strip()
    index = 0
    while(index < len(str)):
        if str[index] == '%':
            str = str[0:index] + urllib2.unquote(str[index:index+3]) + str[index+3:]
        index += 1
    print str