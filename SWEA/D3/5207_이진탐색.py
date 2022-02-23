T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    # B내의 양의 정수가 A에 들어있는지 확인 + 왼쪽 구간/오른쪽 구간 번갈아 탐색한 숫자의 개수
    
    for i in range(M):
        direction = 'm'  # 기본 방향 중앙으로 설정(중앙기준 오른쪽은 'r', 왼쪽은 'l')
        start = 0
        end = N - 1
        target = B[i]
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == B[i]:
                cnt += 1
                break
            elif A[mid] > B[i]:
                end = mid - 1
                if direction == 'l':   
                    break
                direction = 'l'
            else:
                start = mid + 1
                if direction == 'r':
                    break
                direction = 'r'

    print('#{} {}'.format(tc, cnt))