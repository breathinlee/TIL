# sol 1

from itertools import product
from collections import deque

operator = ['+', '-']

def solution(numbers, target):
    answer = 0
    cases = product(operator, repeat=len(numbers))
    for case in cases:
        result = 0
        k = 0
        number = deque(numbers[:])
        while deque and k < len(numbers):
            ret = number.popleft()
                
            if case[k] == '+':
                result += ret
            else:
                result -= ret
            
            k += 1
                    
        if result == target:
            answer += 1
                
    return answer



# sol 2
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx == N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1, numbers, target, value+numbers[idx])
    DFS(idx+1, numbers, target, value-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer