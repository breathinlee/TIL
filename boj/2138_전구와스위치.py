import sys
input = sys.stdin.readline

def change_bulb(k, bulbs):
    if bulbs[k] == '1':
        bulbs[k] = '0'
    else:
        bulbs[k] = '1'


def switch_First(bulbs):
    cnt = 1
    change_bulb(0, bulbs)
    change_bulb(1, bulbs)

    for k in range(1, N):
        if bulbs[k-1] != next[k-1]:
            cnt += 1
            change_bulb(k-1, bulbs)
            change_bulb(k, bulbs)
            if k != N-1:
                change_bulb(k+1, bulbs)

    if bulbs == next:
        return cnt
    return -1


def not_Switch_First(bulbs):
    cnt = 0

    for k in range(1, N):
        if bulbs[k - 1] != next[k - 1]:
            cnt += 1
            change_bulb(k - 1, bulbs)
            change_bulb(k, bulbs)
            if k != N - 1:
                change_bulb(k + 1, bulbs)

    if bulbs == next:
        return cnt
    return -1


N = int(input())
present = list(input().rstrip())
next = list(input().rstrip())

case1 = switch_First(present[:])
case2 = not_Switch_First(present[:])

if case1 != -1 and case2 != -1:
    print(min(case1, case2))
elif case1 == -1:
    print(case2)
elif case2 == -1:
    print(case1)
else:
    print(-1)