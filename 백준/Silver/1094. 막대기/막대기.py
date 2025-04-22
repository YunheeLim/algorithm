x = int(input())

n = 64
answer = 0

while x > 0:
    if n > x:
        n //= 2
    else:
        x -= n
        answer += 1

print(answer)