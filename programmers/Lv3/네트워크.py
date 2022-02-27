# dfs

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


# bfs

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    queue = deque()
    
    for start in range(n):
        if not visited[start]:
            queue.append(start)
            while queue:
                k = queue.pop()
                visited[k] = 1
                
                for s in range(n):
                    if computers[k][s] and not visited[s]:
                        queue.append(s)
            answer += 1
        
    return answer