from itertools import permutations

n = int(input())
lst = list(map(int, input().split()))
operator_input = list(map(int, input().split()))

operators = []

for i in range(len(operator_input)):
    for j in range(operator_input[i]):  
        if i == 0:
            operators.append('+')
        elif i == 1:
            operators.append('-')
        elif i == 2:
            operators.append('*')
        elif i == 3:
            operators.append('/')

orders = set(list(permutations(operators,len(operators))))

max = -int(1e9)
min = int(1e9)

# print(max)

def divide(num1, num2):
    if num1 > 0:
        return num1 // num2
    else:
        num1 = -num1
        return -(num1//num2)

for case in orders:
    cur = 1
    sum = lst[0]
    # print(lst[0], end=' ')

    for operator in case:
        if operator == '+':
            sum += lst[cur]
            # print('+', end=' ')

        elif operator == '-':
            sum -= lst[cur]
            # print('-', end=' ')

        elif operator == '*':
            sum *= lst[cur]
            # print('*', end=' ')

        elif operator == '/':
            # sum = int(sum / lst[cur])
            sum = divide(sum, lst[cur])
            # print('/', end=' ')

        # print(lst[cur], end=' ')

        cur += 1
    #     print('||', sum)
    # print('=', sum)

    if sum > max:
        max = sum
    if sum < min:
        min = sum

print(max)
print(min)

# print(-1//3)
# print(int(-1/3))
