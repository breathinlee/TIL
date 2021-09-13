# 푸른 자성체(B) -> N극 / 붉은 자성체(A) -> S극
# 빨, 파 쌍 하나씩 붙으면 교착상태 +1
# 1: N극 성질(위) / 2: S극 성질(아래)

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        stack = []
        for j in range(N):
            if arr[j][i] == 1:
                if len(stack) == 0:
                    stack.append(arr[j][i])
            elif arr[j][i] == 2:
                if stack:
                    stack.pop()
                    cnt += 1

    print('#{} {}'.format(tc, cnt))