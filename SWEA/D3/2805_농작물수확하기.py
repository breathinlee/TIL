T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    mid = N//2
    my_sum = 0
    start = end = mid
    for i in range(N):
        for j in range(start, end+1):
            my_sum += farm[i][j]
        if i < mid:                         # mid에 도달하기 전까지는 앞으로 -1, 뒤로 +1씩
            start, end = start-1, end+1
        else:                               # mid부터는(다음줄에 적용할 것) 앞으로 +1씩, 뒤로 -1씩
            start, end = start+1, end-1

    print('#{} {}'.format(tc, my_sum))