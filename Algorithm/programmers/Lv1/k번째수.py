def solution(array, commands):
    answer = []
    
    for command in commands:
        slicing_list = array[command[0]-1:command[1]]
        temp = sorted(slicing_list)[command[2]-1]
        answer.append(temp)
        
    return answer


# def solution(arrary, commands):
#   return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))