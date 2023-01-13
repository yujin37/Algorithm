from collections import deque
def dfs(graph):
    visited=[]
    need=deque()
    need.append(1)
    while need:
        node=need.popleft()
        if node not in visited:
            visited.append(node)
            need.extend(graph[node])
    return visited
com=int(input())
sang=int(input())
network=dict()
for i in range(1,com+1):
    network[i]=[]
#print(network)
for i in range(sang):
    n1,n2=map(int,input().split())
    network[n1].append(n2)
    network[n2].append(n1)
#print(network)
result=dfs(network)
print(len(result)-1)
#print(result)


