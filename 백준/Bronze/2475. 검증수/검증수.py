lst = list(map(int, input().split()))

result = 0

for num in lst:
    result += num * num

print(result % 10)