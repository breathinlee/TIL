def dfs(start, computers, visited): 
    visited[start] = 1
    
    for k in range(len(computers)):
        if computers[start][k] and not visited[k]:
            dfs(k, computers, visited)
                

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for r in range(n):
        if not visited[r]:
            dfs(r, computers, visited)
            answer += 1
    return answer