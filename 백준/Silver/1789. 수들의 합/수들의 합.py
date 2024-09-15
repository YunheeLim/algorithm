s = int(input())

sum = 0
# cnt = 0
i = 0
while sum <= s:
    i += 1
    sum += i

print(1 if s == 1 else i - 1)