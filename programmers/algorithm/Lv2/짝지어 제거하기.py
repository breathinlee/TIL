from collections import deque

def solution(s):
    answer = 0

    s = deque(s)
    out = deque()

    while s:
        alphabet = s.popleft()

        if len(out):
            if alphabet == out[-1]:
                out.pop()
            else:
                out.append(alphabet)
        else:
            out.append(alphabet)

    if len(out) == 0:
        answer = 1

    return answer
