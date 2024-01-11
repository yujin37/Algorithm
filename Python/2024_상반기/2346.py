from collections import deque
n = int(input())

ballon = deque(enumerate(map(int,input().split())))

now = 0
visited = [False for _ in range(n)]
result = []

while ballon:
    idx, paper = ballon.popleft()
    
    result.append(idx+1)
    
    if paper > 0:
        ballon.rotate(-(paper-1))
    else:
        ballon.rotate(-paper)
print(*result)
    