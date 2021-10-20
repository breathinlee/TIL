# so1 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    value = list(map(int, input().split()))
    ret = 0
    
    while len(value) > 0:
        max_value = max(value)
        max_value_idx = value.index(max_value)
        if max_value_idx == 0:
            value.pop(0)
            continue
        for i in range(max_value_idx):
            ret += max_value - value[i]
        value = value[max_value_idx+1:N]
    print('#{} {}'.format(tc, ret))



# sol 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    value = list(map(int, input().split()))
    value.reverse()
    benefit = 0
    max_val = value[0]

    for i in range(1, N):
        if max_val < value[i]:
            max_val = value[i]

        else:
            benefit += max_val - value[i]

    print('#{} {}'.format(tc, benefit))