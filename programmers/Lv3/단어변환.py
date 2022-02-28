# ver1 (미완성)

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    queue = deque([begin])
    
    while queue:
        tmp = queue.popleft()
        
        if tmp == target:
            return answer
        
        for word in words:
            cnt = 0
            for k in range(len(begin)):
                if word[k] != tmp[k]:
                    cnt += 1
                if cnt >= 2:
                    break
            if cnt == 1:
                queue.append(word)
                words.remove(word)
        answer += 1
        
    
    return answer