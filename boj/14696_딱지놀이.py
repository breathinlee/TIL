# 별, 동그라미, 네모, 세모를 각각 숫자 4, 3, 2, 1
N = int(input())    # 라운드 개수
for i in range(1, N+1):
    card_a = input().split()
    card_b = input().split()
    card_a_cnt = [0] * 5
    card_b_cnt = [0] * 5
    for j in range(1, len(card_a)):
        card_a_cnt[int(card_a[j])] += 1
    for j in range(1, len(card_b)):
        card_b_cnt[int(card_b[j])] += 1
    if card_a_cnt == card_b_cnt:
        winner = 'D'
    for k in range(4, 0, -1):
        if card_a_cnt[k] < card_b_cnt[k]:
            winner = 'B'
            break
        elif card_a_cnt[k] == card_b_cnt[k]:
            continue
        elif card_a_cnt[k] > card_b_cnt[k]:
            winner = 'A'
            break

    print(winner)