from collections import deque
n=int(input())
tree= [[] for _ in range(n+1)]
for i in range(n-1):
    n1,n2=map(int,input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)
visited=[0]*(n+1)

def bfs():
    visited[1]=1
    queue=deque()
    queue.append(1)
    while queue:
        u=queue.popleft()
        #print(u)
        for node in tree[u]:
            if visited[node]==0:
                visited[node]=u
                queue.append(node)
bfs()
for num in range(2,n+1,1):
    print(visited[num])
    
#tree.sort()
#print(tree)

