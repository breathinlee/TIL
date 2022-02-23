# 5개의 숫자중 3자리의 순열 생성하기

def permutation(n, k, m):     # n: 자리 인덱스, k: 순열 길이, m: 주어진 숫자 개수
    if n == k:
        print(*numbers[:3])
    else:
        for i in range(n, m):
            numbers[n], numbers[i] = numbers[i], numbers[n]
            permutation(n+1, k, m)
            numbers[n], numbers[i] = numbers[i], numbers[n]


numbers = [1, 2, 3, 4, 5]
permutation(0, 3, 5)