def find_winner(start, end):
    if start == end:
        return start

    mid = (start + end) // 2
    left = find_winner(start, mid)
    right = find_winner(mid+1, end)

    if cards[right] - cards[left] == -2 or cards[right] - cards[left] == 1:
        return right
    else:
        return left


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))

    ans = find_winner(1, N)
    print('#{} {}'.format(tc, ans))