def solution(arr):
    answer = [arr[0]]
    idx = 1
    
    while idx < len(arr):
        if arr[idx] != answer[-1]:
            answer.append(arr[idx])
        else:
            pass
        idx += 1
    
    return answer