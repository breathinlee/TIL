# tc 1,2 시간 초과..

def solve(departure, airline_tickets, visited, tickets):
    global answer
    
    while True:
        if 0 not in visited:
            return
        
        for idx2, w in enumerate(airline_tickets[departure]):
            idx = tickets.index([departure, w])
            visited[idx] = 1
            answer.append(w)
            airline_tickets[departure].pop(idx2)
            solve(w, airline_tickets, visited, tickets)
        
        
answer = ['ICN']

def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    visited = [0] * len(tickets)
    airline_tickets = {}
    for ticket in tickets:
        if ticket[0] not in airline_tickets:
            airline_tickets[ticket[0]] = [ticket[1]]
        else:
            airline_tickets[ticket[0]].append(ticket[1])
            
    solve('ICN', airline_tickets, visited, tickets)
    
    return answer



# tc 1, 2 시간초과 2

from collections import defaultdict

def solve(departure, airline_tickets, visited, tickets):
    global answer
    
    while True:
        if 0 not in visited:
            return
        
        for idx2, w in enumerate(airline_tickets[departure]):
            idx = tickets.index([departure, w])
            visited[idx] = 1
            answer.append(w)
            airline_tickets[departure].pop(idx2)
            solve(w, airline_tickets, visited, tickets)
        
        
answer = ['ICN']

def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    visited = [0] * len(tickets)
    airline_tickets = defaultdict(list)
    for ticket in tickets:
        if ticket[0] not in airline_tickets:
            airline_tickets[ticket[0]] = [ticket[1]]
        else:
            airline_tickets[ticket[0]].append(ticket[1])
            
    solve('ICN', airline_tickets, visited, tickets)
    
    return answer


# tc 1 런타임에러

def solve(departure, airline_tickets, visited, tickets):
    global answer

    while True:
        if 0 not in visited:
            return

        if len(airline_tickets[departure]) == 0:
            return

        for idx2, w in enumerate(airline_tickets[departure]):
            if airline_tickets[departure][idx2] in airline_tickets or len(airline_tickets[departure]) == 1:
                idx = tickets.index([departure, w])
                visited[idx] = 1
                answer.append(w)
                airline_tickets[departure].pop(idx2)
                solve(w, airline_tickets, visited, tickets)


answer = ['ICN']

def solution(tickets):
    visited = [0] * len(tickets)
    airline_tickets = {}
    for ticket in tickets:
        if ticket[0] not in airline_tickets:
            airline_tickets[ticket[0]] = [ticket[1]]
        else:
            airline_tickets[ticket[0]].append(ticket[1])

    for key in airline_tickets:
        airline_tickets[key].sort()

    solve('ICN', airline_tickets, visited, tickets)

    return answer
