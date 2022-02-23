T = int(input())
for tc in range(1, T+1):
    N = int(input())
    document = ''
    for _ in range(N):
        alphabet, k = input().split()
        K = int(k)
        document += alphabet * K

    # print(document)

    print('#{}'.format(tc))

    for i in range(0, len(document), 10):
        print(document[i:i+10])