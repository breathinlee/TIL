def distance(go, now):
    key_pad =  {1: [0, 0], 2: [1, 0], 3: [2, 0],
              4: [0, 1], 5: [1, 1], 6: [2, 1],
              7: [0, 2], 8: [1, 2], 9: [2, 2],
              "*": [0, 3], 0: [1, 3], "#": [2, 3], }
    
    x1, y1 = key_pad[go]
    x2, y2 = key_pad[now]
    
    return abs(x1 - x2) + abs(y1 - y2)
    

def solution(numbers, hand):
    answer = ''
    left_position = '*'
    right_position = '#'
    
    left_side = [1, 4, 7]
    right_side = [3, 6, 9]
    
    for number in numbers:
        if number in left_side:
            answer += 'L'
            left_position = number
        elif number in right_side:
            answer += 'R'
            right_position = number
        else:
            if distance(number, left_position) < distance(number, right_position):
                answer += 'L'
                left_position = number
            elif distance(number, left_position) > distance(number, right_position):
                answer += 'R'
                right_position = number
            else:
                if hand == 'left':
                    answer += 'L'
                    left_position = number
                else:
                    answer += 'R'
                    right_position = number
            
    return answer