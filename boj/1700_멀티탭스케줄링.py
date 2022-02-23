N, K = map(int, input().split())
machines = list(map(int, input().split()))

cnt = 0
plug = []

for idx, machine in enumerate(machines):
    if machine in plug:
        continue
    elif len(plug) < N:
        plug.append(machine)
    else:
        substitute = 0
        position = -1
        leaves = machines[idx:]
        for p in plug:
            if p not in leaves:
                substitute = p
                break
            else:
                target = leaves.index(p)
                if position < target:
                    position = target
                    substitute = p
        plug[plug.index(substitute)] = machine
        cnt += 1

print(cnt)