n = int(input())
stack = list()
for i in range(n):
    how_to = list(map(int,input().split()))
    if how_to[0] == 1: #스택에 넣는다.
        stack.append(how_to[1])
    elif how_to[0] == 2: 
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif how_to[0] == 3:
        print(len(stack))
    elif how_to[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif how_to[0] == 5:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    