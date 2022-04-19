def solution(N, number):
    arr = [set() for _ in range(8)]
    for idx, S in enumerate(arr, start=1):
        S.add(int(str(N) * idx))

    for i in range(8):
        for j in range(i):
            for a in arr[j]:
                for b in arr[i-j-1]:
                    arr[i].add(a + b)
                    arr[i].add(a - b)
                    arr[i].add(a * b)
                    if b != 0:
                        arr[i].add(a // b)

        if number in arr[i]:
            return i + 1

        answer = -1

    return answer