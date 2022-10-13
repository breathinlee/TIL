sugar = int(input())
total = 0

while sugar > 0:
    if sugar % 5 == 0:
        total += (sugar // 5)
        print(total)
        break

    sugar -= 3
    total += 1

else:
    print(-1) if sugar else print(total)