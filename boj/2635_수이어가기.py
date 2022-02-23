first = int(input())
max_cnt = 0
result = []
for i in range(first, 0, -1):
    number_list = [first]
    number_list.append(i)
    idx = 0
    while number_list[idx] - number_list[idx+1] >= 0:
        number_list.append(number_list[idx] - number_list[idx+1])
        idx += 1
    if max_cnt < len(number_list):
        max_cnt = len(number_list)
        result = number_list[:]

print(max_cnt)
for num in result:
    print(num, end=' ')