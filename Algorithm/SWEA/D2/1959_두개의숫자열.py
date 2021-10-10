T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))  # 길이 N
    B_list = list(map(int, input().split()))  # 길이 M

    if N <= M:
        sum_list = []
        for i in range(M-N+1):
            my_sum = 0
            for j in range(N):
                my_sum += A_list[j] * B_list[j+i]
            sum_list.append(my_sum)
        print('#{} {}'.format(tc, max(sum_list)))

    else:                       # N > M
        sum_list = []
        for i in range(N-M+1):
            my_sum = 0
            for j in range(M):
                my_sum += B_list[j] * A_list[j+i]
            sum_list.append(my_sum)
        print('#{} {}'.format(tc, max(sum_list)))