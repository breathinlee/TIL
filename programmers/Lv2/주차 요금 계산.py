import math

def calculate_time(arr):
    total = 0
    
    if len(arr) % 2:
        arr.append('23:59')
        
    for i in range(0, len(arr)-1, 2):
        in_h, in_m = map(int, arr[i].split(':'))
        out_h, out_m = map(int, arr[i+1].split(':'))
        
        if in_m > out_m:
            out_h -= 1
            out_m += 60
            
        total += ((out_h - in_h) * 60 + out_m - in_m)
        
    return total
        

def calculate_cost(fees, minutes):
    cost = fees[1]
    
    if minutes > fees[0]:
        cost += math.ceil((minutes - fees[0])/fees[2]) * fees[3]
        
    return cost     


def solution(fees, records):
    answer = []
    garage = {}
    
    for record in records:
        time, car_number, history = record.split(' ')
        if car_number not in garage:
            garage[car_number] = [time]
        else:
            garage[car_number].append(time)
    
    for g in garage:
        tmp = calculate_time(garage[g])
        garage[g] = tmp
            
    garage = sorted(garage.items())
    
    for g in garage:
        answer.append(calculate_cost(fees, g[1]))
    
    return answer