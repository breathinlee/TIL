import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())  # 트럭수 / 다리길이 / 다리 하중
trucks = list(map(int, input().split()))

time = 0
bridge = [0] * w

while True:
    truck = bridge.pop(0)
    L += truck

    if trucks and L >= trucks[0]:
        next = trucks.pop(0)
        bridge.append(next)
        L -= next

    else:
        bridge.append(0)

    time += 1

    if not trucks and bridge.count(0) == w:
        break

print(time)