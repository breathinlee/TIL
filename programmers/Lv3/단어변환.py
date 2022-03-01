# sol
def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    stack = [begin]

    while len(words):
        for s in stack:
            next = []
            for word in words:
                cnt = 0
                for k in range(len(begin)):
                    if word[k] != s[k]:
                        cnt += 1
                    if cnt >= 2:
                        break
                if cnt == 1:  # begin이 words안에 존재할 수 있음
                    next.append(word)
                    words.remove(word)
        answer += 1

        if target in next:
            return answer
        stack = next

    return answer





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

