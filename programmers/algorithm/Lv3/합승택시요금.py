import sys

INF = sys.maxsize

def solution(n, s, a, b, fares):
    answer = INF
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
        
    for fare in fares:
        start, end, f = fare
        dist[start][end] = f
        dist[end][start] = f
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    for i in range(1, n+1):
        answer = min(answer, dist[i][s] + dist[i][a] + dist[i][b])
    
    return answer