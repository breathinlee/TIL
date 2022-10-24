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