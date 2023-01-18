import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
visited=[]
def dfs(graph, start):
    global visited
    need=deque()
    need.append(start)
    while need:
        node = need.pop()
        if node not in visited:
            visited.append(node)
            need.extend(graph[node])
    
con={}
for i in range(1,n+1):
    con[i]=[]
for i in range(m):
    u,v=map(int,input().split())
    con[u].append(v)
    con[v].append(u)
cnt=1
re=0
while cnt <=n:
    if cnt not in visited:
        dfs(con, cnt)
        
        re+=1
    cnt+=1
print(re)
