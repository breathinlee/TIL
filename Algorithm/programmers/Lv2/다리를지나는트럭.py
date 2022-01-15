def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * (bridge_length)

    while truck_weights or weight or sum(bridge):
        truck = bridge.pop(0)
        weight += truck

        if truck_weights and weight - truck_weights[0] >= 0:
            new_truck = truck_weights.pop(0)
            bridge.append(new_truck)
            weight -= new_truck

        else:
            bridge.append(0)

        time += 1

        if len(truck_weights) == 0 and bridge == [0] * (bridge_length):
            break

    return time