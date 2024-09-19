from itertools import combinations

n = int(input())

lst = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(list(map(str, reversed(list(j)))))
        lst.append(int(num))

lst.sort()

try:
    print(lst[n])
except:
    print(-1)