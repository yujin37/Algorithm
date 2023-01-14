from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(ground, a, b):
    queue = deque()
    queue.append((a,b))
    ground[a][b]=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if ground[nx][ny]==1:
                ground[nx][ny]=0
                queue.append((nx,ny))
    return
t=int(input())

for i in range(t):
    cnt=0
    m,n,k=map(int,input().split())
    ground=[[0 for _ in range(m)] for _ in range(n)]
    for j in range(k):
        x,y=map(int,input().split())
        ground[y][x]=1
    for k in range(n):
        for l in range(m):
            if ground[k][l]==1:
                bfs(ground, k, l)
                cnt+=1
    print(cnt)