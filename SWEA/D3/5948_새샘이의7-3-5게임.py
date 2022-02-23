from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    cases = list(combinations(numbers, 3))
    ret = []
    for case in cases:
        ret.append(sum(case))
    ret = list(set(ret))
    ret.sort(reverse=True)
    print('#{} {}'.format(tc, ret[4]))