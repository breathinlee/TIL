import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    values = list(int(input()) for _ in range(N))
    ans = 0

    for j in range(N-1, -1, -1):
        ans += (K // values[j])
        K %= values[j]

    print(ans)