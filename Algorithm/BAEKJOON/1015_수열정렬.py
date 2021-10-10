N = int(input())
numbers = list(map(int, input().split()))
c_numbers = numbers.copy()
c_numbers.sort()
idx_list = []
for i in numbers:
    cnt = 0
    # idx_list.append(c_numbers.index(i) + cnt)
    while numbers[-1]:
        if c_numbers.index(i) + cnt in idx_list:
            cnt += 1
        else:
            break
    idx_list.append(c_numbers.index(i) + cnt)
print(*idx_list)   
