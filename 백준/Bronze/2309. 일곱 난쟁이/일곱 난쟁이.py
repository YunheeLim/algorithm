import sys
sys.stdin.readline

lst = []

for _ in range(9):
    lst.append(int(input()))

lst.sort()

escape = False

for i in range(8):
    for j in range(i+1, 9):
  
        if (sum(lst) - lst[i] - lst[j]) == 100:
            lst.remove(lst[j])
            lst.remove(lst[i])
            escape = True
            break
    if escape:
        break
   

for elem in lst:
    print(elem)