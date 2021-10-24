# 부분집합 구현

def print_set(n):
    global cnt_subset
    cnt_subset += 1
    print('{}: '.format(cnt_subset), end='')

    for i in range(n):
        if check[i] == 1:
            print(numbers[i], end=' ')
    print()


def powerset(n, k):       # n: 현재 depth, k: 원소 개수
    if n == k:
        print_set(n)
    else:
        check[n] = 1      # n번 요소 포함시킴
        powerset(n+1, k)  # 다음 요수 포함 여부 결정위한 호출
        check[n] = 0      # n번 요소 포함x
        powerset(n+1, k)  # 다음 요소 포함 여부 결정위한 호출
    

cnt_subset = 0             # 생성되는 부분집합 수 확인용
numbers = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(numbers)
check = [0] * N

powerset(0, N)