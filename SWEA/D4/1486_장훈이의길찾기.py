def find_height(idx, height):
    global min_height
    if height - B > min_height:
        return
    if idx == N:                                         # 배열을 다 돌았을 떄
        if height - B >= 0:
            min_height = height - B
            return
    else:
        # visited[idx] = 1
        find_height(idx+1, height+people_height[idx])    # 인덱스에 해당하는 점원 키 포함
        # visited[idx] = 0
        find_height(idx+1, height)                       # 인덱스에 해당하는 점원 키 포함X


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())   # N: 점원의 수 / B: 선반의 높이(1 <= B <= S(점원들 키 합))
    people_height = list(map(int, input().split()))
    min_height = 200000
    # visited = [0] * N
    find_height(0, 0)
    print('#{} {}'.format(tc, min_height))