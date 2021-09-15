T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    # W : 한 달 수도 양
    # P : A사 1리터당 요금
    # Q : B사 기본 요금
    # R : B사 기본 요금 청구되는 사용량
    # S : B사 R보다 많은 양 사용 시 초과량에 대한 1리터당 요금

    A_price = P * W
    if R < W:
        B_price = Q + (W - R) * S
    else:
        B_price = Q

    print('#{} {}'.format(tc, min(A_price, B_price)))