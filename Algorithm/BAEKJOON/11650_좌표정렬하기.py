import sys

N = int(sys.stdin.readline())
list = []
for i in range(N):
    x, y = map(int, sys.stdin.readline(). split())
    list.append([x, y])
list.sort()
for data in list:    
    print(data[0], data[1])

