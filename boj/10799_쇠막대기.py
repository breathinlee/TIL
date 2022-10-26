import sys
input = sys.stdin.readline

iron_stick = input().rstrip()
lazer = False
stick = 0
cnt = 0

for i in range(len(iron_stick)):
    if iron_stick[i] == '(':
        if iron_stick[i+1] == ')':
            lazer = True
        else:
            stick += 1
    else:
        if lazer:
            cnt += stick
            lazer = False
        else:
            cnt += 1
            stick -= 1

print(cnt)