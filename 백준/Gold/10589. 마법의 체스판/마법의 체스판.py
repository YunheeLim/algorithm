n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

k = n // 2 + m // 2

results= []

for col in range(2, m+1, 2):
    results.append((1, col, n, col))

for row in range(2, n+1, 2):
    results.append((row, 1, row, m))

print(k)

for result in results:
    for i in result:
        print(i, end=" ")
    print()