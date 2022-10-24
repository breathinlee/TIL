# sol 1 (4876ms)

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    members_score = [list(map(int, input().rstrip().split())) for _ in range(N)]
    sorted_members_score = sorted(members_score, key=lambda x: x[0])

    result = 1
    standard = sorted_members_score[0][1]

    for k in range(1, N):
        if sorted_members_score[k][1] < standard:
            result += 1
            standard = sorted_members_score[k][1]

    print(result)



# sol 2 (2452ms + 메모리도 절반 이하)

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    members_rank = [0] * (N+1)
    for _ in range(N):
        first, second = map(int, input().rstrip().split())
        members_rank[first] = second

    result = 0
    standard = N+1

    for k in range(1, N+1):
        if members_rank[k] < standard:
            result += 1
            standard = members_rank[k]

    print(result)