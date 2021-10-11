from itertools import combinations

fake_dwarfs = []
for _ in range(9):
    number = int(input())
    fake_dwarfs.append(number)

cases = list(combinations([i for i in range(0, 9)], 7))
for case in cases:
    case_sum = 0
    for j in range(7):
        case_sum += fake_dwarfs[case[j]]
    if case_sum == 100:
        true_case = case
        break

# print(true_case)
true_dwarfs = []
for k in true_case:
    true_dwarfs.append(fake_dwarfs[k])
true_dwarfs.sort()
for num in true_dwarfs:
    print(num)