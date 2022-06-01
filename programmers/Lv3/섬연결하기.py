def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    answer = costs[0][2]
    check = set([costs[0][0], costs[0][1]])

    while len(check) < n:
        for k in range(1, len(costs)):
            if costs[k][0] in check and costs[k][1] in check:
                continue
            elif costs[k][0] in check or costs[k][1] in check:
                check.update([costs[k][0], costs[k][1]])
                answer += costs[k][2]
                break

    return answer