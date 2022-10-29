def solution(clothes):
    cloth_type = {}
    result = 1
    
    for cloth in clothes:
        if cloth[1] not in cloth_type:
            cloth_type[cloth[1]] = [cloth[0]]
        else:
            cloth_type[cloth[1]].append(cloth[0])
     
    for key in cloth_type.keys():
        result *= (len(cloth_type[key]) + 1)
    
    return result - 1