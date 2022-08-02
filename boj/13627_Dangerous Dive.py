import sys
input = sys.stdin.readline

N, R = map(int, input().split())
returned_volunteers = list(map(int, input().split()))

volunteers = [i for i in range(1, N+1)]

if volunteers == sorted(returned_volunteers):
    print('*')
else:
    for v in volunteers:
        if v not in returned_volunteers:
            print(v, end=' ')