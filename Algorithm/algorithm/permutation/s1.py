numbers = [1, 2, 3]

for i in numbers:
    for j in numbers:
        if i != j:
            for k in numbers:
                if j != k and i != k:
                    print(i, j, k)