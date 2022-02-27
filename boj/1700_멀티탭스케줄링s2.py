N, K = map(int, input().split())
machines = list(map(int, input().split()))

cnt = 0
plug = []

for i in range(K):
    if machines[i] in plug:
        continue

    elif len(plug) < N:
        plug.append(machines[i])

    else:
        target = []
        target_idx = []
        leaves = machines[i:]
        for p in plug:
            if p in leaves:
                target.append(p)
                target_idx.append(leaves.index(p))
            else:
                target.append(p)
                target_idx.append(101)
        max_idx = target_idx.index(max(target_idx))
        plug[max_idx] = machines[i]
        cnt += 1

print(cnt)