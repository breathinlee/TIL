import sys
input = sys.stdin.readline

def calculate(min_height, hills):
    ret = 0

    for hill in hills:
        if hill < min_height:
            ret += (min_height - hill) ** 2

        elif hill > min_height + 17:
            ret += (hill - (min_height + 17)) ** 2

    return ret

N = int(input())
hills = [int(input()) for _ in range(N)]

ans = 987654321

if max(hills) - min(hills) <= 17:
    print(0)
else:
    for k in range(min(hills), max(hills) - 17):
        ans = min(ans, calculate(k, hills))
    print(ans)