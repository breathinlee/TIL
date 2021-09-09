T = int(input())
for tc in range(1, T+1):
    time = list(map(int, input().split()))
    hour = 0
    minute = 0

    for idx in range(4):
        if idx % 2:
            minute += time[idx]
        else:
            hour += time[idx]

    if minute > 60:
        hour += minute // 60
        minute = minute % 60

    if hour % 12:
        hour = hour % 12
    else:
        hour = 12

    print('#{} {} {}'.format(tc, hour, minute))