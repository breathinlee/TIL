import sys
input = sys.stdin.readline

N, M = map(int, input().split())
notHeard = dict()
notHeardSeen = dict()

for _ in range(N):
    name = input()
    notHeard[name] = 1

for _ in range(M):
    name = input()
    if name in notHeard:
        notHeardSeen[name] = 1

print(len(notHeardSeen))
for name in sorted(notHeardSeen):
    print(name, end='')