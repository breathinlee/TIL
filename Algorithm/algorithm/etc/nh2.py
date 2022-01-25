def solve(arr):
    answer = dict()
    result = 0

    for k in arr:
        k = tuple(k)
        if k in answer:
            answer[k] += 1
        else:
            answer[k] = 1

    for key, value in answer.items():
        if value > 1:
            result += (value - 1)

    return result


print(solve([[4, 3], [2, 1], [1, 2], [4, 3], [4, 3], [1, 2]]))
print(solve([[1, 1], [1, 1], [1, 1]]))
print(solve([[1, 1], [2, 1], [1, 2], [2, 2]]))

# output
# 3
# 2
# 0