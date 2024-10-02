import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.list=[]

    def __len__(self):
        return len(self.list)

    def push(self, X):
        self.list.append(X)

    def pop(self):
        if len(self.list) == 0:
            print(-1)
        else:
            print(self.list.pop(-1))

    def size(self):
        print(len(self.list))

    def empty(self):
        if len(self.list)==0:
            print(1)
        else:
            print(0)

    def top(self):
        if len(self.list)==0:
            print(-1)
        else:
            print(self.list[-1])


N =  int(input())
stack1 = Stack()

for i in range(N):

    a = input().strip()

    if "push" in a:
        num = a[5:len(a)]
        stack1.push(num)

    elif a=="pop":
        stack1.pop()
        
    elif a=="size":
        stack1.size()

    elif a=="empty":
        stack1.empty()

    elif a=="top":
        stack1.top()
    
    else:
        print("Error")