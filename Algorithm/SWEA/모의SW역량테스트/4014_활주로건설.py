# 미완성

"""
생각한 방법 1
1. 연결된 부분의 숫자의 차이가 1보다 크면 fail
2. max값보다 작은 특정 숫자의 개수가 X개보다 작으면 fail
3. 숫자가 바뀌는 점 표시하여 양옆으로 X개씩 확인하며 방문표시해서 경사로 간 겹치지 않도록 할 것
4. 함수로 처리하여 행/열에 대해 수행


생각한 방법 2
1-3. 배열 첫 값과 비교하여 크거나 작은 경우 나눠서 경사로 놓을 수 있을지 확인

생각한 방법 3
숫자가 바뀌는 점 표시한 배열이용
- 1이 맨 끝에 있는 경우 fail (적어도 -x-1번에서 나오고 그 뒤 0이어야 가능)
- 11의 경우 두 양쪽 확인
- 111 이상의 경우 fail

....
"""

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())   # N : 지도의 한 변의 크기 X : 경사로 길이  (단, 경사로 높이는 1로 고정)
    road = [list(map(int, input().split())) for _ in range(N)]

    # 행 탐색 시작  => 열에도 똑같이 적용
    for i in range(N):
        max_value = max(road[i])
        max_idx = road[i].index(max_value)
        cnt = 0
        check = [0] * N
        for j in range(N-1):
            # 연결된 부분의 숫자의 차이가 1보다 크면 fail
            if abs(road[i][j] - road[i][j+1]) > 1:
                break
            # 행이 모두 같은 숫자로 이루어진 경우 활주로 O
            elif road[i].count(road[i][0]) == N:
                cnt += 1
                break
            # 값 비교
            else:
                tmp = road[i][0]
                if tmp < road[i][j]:



