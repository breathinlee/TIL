from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        price = prices.popleft()
        result = 0
        
        result = 0
        for p in prices:
            if price <= p:
                result += 1
            else:
                result += 1
                break
        
        answer.append(result)
            
    return answer