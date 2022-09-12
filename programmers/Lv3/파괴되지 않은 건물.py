# 누적합 이용

def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    arr = [[0] * (m+1) for _ in range(n+1)]
    
    for s in skill:
        if s[0] == 1:
            arr[s[1]][s[2]] -=s[5] 
            arr[s[3]+1][s[4]+1] -=s[5]
            arr[s[3]+1][s[2]] += s[5] 
            arr[s[1]][s[4]+1] += s[5]
            
        else:
            arr[s[1]][s[2]] += s[5] 
            arr[s[3]+1][s[4]+1] += s[5]
            arr[s[3]+1][s[2]] -= s[5]
            arr[s[1]][s[4]+1] -= s[5]
    
    for i in range(n):
        for j in range(m):
            arr[i][j+1] += arr[i][j]
            
    for j in range(m):
        for i in range(n):
            arr[i+1][j] += arr[i][j]
            
    for r in range(n):
        for c in range(m):
            if arr[r][c] + board[r][c] > 0:
                answer += 1
                
    return answer