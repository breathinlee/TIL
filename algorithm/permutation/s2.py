# recursion (swap)

def permutation_by_swap(n, k):   # n: 숫자를 결정할 자리 / k: 순열의 길이
    if n == k:                   # 모든 자리가 확정된 경우
        print(*numbers)
    else:
        for i in range(n, k):    # 자기 자신부터 맨 마지막자리까지 순서대로 교환하기 위함
            numbers[n], numbers[i] = numbers[i], numbers[n] 
            permutation_by_swap(n+1, k)                       # 다음 번 자리 결정하러 이동
            numbers[n], numbers[i] = numbers[i], numbers[n]   # 교환 전으로 원상 복구


numbers = [1, 2, 3]
permutation_by_swap(0, 3)
