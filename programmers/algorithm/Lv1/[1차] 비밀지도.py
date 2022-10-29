def solution(n, arr1, arr2):
    answer = []
    for k in range(n):
        temp1 = bin(arr1[k])[2:]
        temp2 = bin(arr2[k])[2:]
        if len(temp1) != n or len(temp2) != n:
            arr1[k] = '0' * (n-len(temp1)) + temp1
            arr2[k] = '0' * (n-len(temp2)) + temp2
        else:
            arr1[k] = temp1
            arr2[k] = temp2
    
    for k in range(n):
        result = ''
        for s in range(n):
            if arr1[k][s] == '0' and arr2[k][s] == '0':
                result += ' '
            else:
                result += '#'
        answer.append(result)
                    
    return answer