T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())   # N명의 사람, M초의 시간동안 K개의 붕어빵 만들 수 있음
    people_come = list(map(int, input().split()))
    people_come.sort()

    people_count = [0] * (people_come[-1] + 1)
    for coming in people_come:
        people_count[coming] += 1
    bbang = 0
    time = 0
    ans = 'Possible'

    # M초마다 K개씩 생성 => M초에 K개, 2M초에 2K개, 3M초에 3K개...
    while time <= people_come[-1]:
        if time > 0 and time % M == 0:
            bbang += K
        if people_count[time] > 0:
            bbang -= people_count[time]
        if bbang < 0:
            ans = 'Impossible'
            break
        time += 1

    print('#{} {}'.format(tc, ans))