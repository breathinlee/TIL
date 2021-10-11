N = int(input())    # 색종이 장 수
check = [[0] * 1001 for _ in range(1001)]
for n in range(1, N+1):
    # 가장 왼쪽 아래 칸의 번호와 너비, 높이를 나타내는 네 정수로 표현
    paper = list(map(int, input().split()))
    for i in range(paper[0], paper[0]+paper[2]):
        for j in range(paper[1], paper[1]+paper[3]):
            check[i][j] = n

for n in range(1, N+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if check[i][j] == n:
                cnt += 1
    print(cnt)