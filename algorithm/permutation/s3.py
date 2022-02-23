# recursion (visited)

def permutation_visited(k):
    if n == k:
        print(*temp)
        return
    else:
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = 1
            temp[k] = numbers[i]
            permutation_visited(k+1)
            visited[i] = 0


numbers = [1, 2, 3]
n = len(numbers)
visited = [0] * n         # 방문 체크용
temp = [0] * n            # 실제 값 할당할 리스트 생성
permutation_visited(0)