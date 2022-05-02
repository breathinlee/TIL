import sys

input = sys.stdin.readline


def find_prev(s):
    if s == 'B':
        return 'J'
    elif s == 'O':
        return 'B'
    else:
        return 'O'


T = int(input())
for _ in range(T):
    N = int(input())
    blocks = input()
    dp = [0] + [10e8] * N

    for i in range(1, N):
        prev_word = find_prev(blocks[i])
        for j in range(i):
            if blocks[j] == prev_word:
                dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

    if dp[N - 1] != 10e8:
        print(dp[N - 1])
    else:
        print(-1)