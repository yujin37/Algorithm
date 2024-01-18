n = int(input())
top = list(map(int,input().split()))
stack = []
result = [0 for _ in range(n)] #신호 받기 기록
for i in range(n):
    while stack:
        if top[stack[-1][0]] < top[i]:
            stack.pop()
        else:
            result[i] = stack[-1][0] + 1
            break
    stack.append([i,top[i]])
print(*result)