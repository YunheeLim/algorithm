t = int(input())


while t:
    n = int(input())

    binary = []
    while n:
        binary.append(n % 2)

        n = int(n / 2)

    for i in range(len(binary)):
        if binary[i] == 1:
            print(i, end=" ")

    t -= 1