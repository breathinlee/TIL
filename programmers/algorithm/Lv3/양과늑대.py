def dfs(node, sheep, wolf, G, info, nodes):
    global answer
    
    if info[node]:
        wolf += 1
    else:
        sheep += 1
        
    if sheep <= wolf:
        return
    
    answer = max(answer, sheep)
    
    for n in nodes:
        for m in G[n]:
            if m not in nodes:
                nodes.append(m)
                dfs(m, sheep, wolf, G, info, nodes)
                nodes.remove(m)
    
                
# 0: 양 / 1: 늑대

answer = 0
def solution(info, edges):  
    G = [[] for _ in range(len(info))]
    
    for edge in edges:
        G[edge[0]].append(edge[1])
        
    dfs(0, 0, 0, G, info, [0])
        
    return answer