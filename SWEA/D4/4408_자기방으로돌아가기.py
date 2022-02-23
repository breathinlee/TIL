T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    corridor = [0] * 201

    for room1, room2 in rooms:
        c_room1 = (room1+1) // 2
        c_room2 = (room2+1) // 2
        if c_room1 <= c_room2:
            for i in range(c_room1, c_room2+1):
                corridor[i] += 1
        else:
            for i in range(c_room2, c_room1+1):
                corridor[i] += 1

    print('#{} {}'.format(tc, max(corridor)))