T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())                # N : 화덕의 크기, M : 피자 개수
    cheese = list(map(int, input().split()))
    pizza = [[idx, val] for idx, val in enumerate(cheese, start=1)]

    in_oven = pizza[:N]
    out_oven = pizza[N:]
    while len(in_oven) > 1:
        rotate_oven = in_oven.pop(0)
        rotate_oven[1] //= 2
        if rotate_oven[1] > 0:
            in_oven.append(rotate_oven)
        else:
            if len(out_oven) != 0:
                in_oven.append(out_oven.pop(0))
    print('#{} {}'.format(tc, in_oven[0][0]))