import sys
input = sys.stdin.readline
from collections import deque
n, m, v = map(int,input().split())
dfs_visited = [0 for _ in range(n+1)]
dfs_index = []
bfs_visited = [0 for _ in range(n+1)]
bfs_index = []
def dfs(n, node, start):
    global dfs_visited
    dfs_index.append(start)
    if not start in node.keys():
        return dfs_index
    dfs_visited[start] = 1  
    
    
    for i in node[start]:
        if dfs_visited[i] ==0:    
            dfs(n, node, i)
        else:
            continue
    return dfs_index
def bfs(n, node, start):
    global bfs_visited
    queue = deque([start])
    bfs_index.append(start)
    if not start in node.keys():
        return bfs_index
    bfs_visited[start] = 1
    
    while queue:
        v = queue.popleft()
        for i in node[v]:
            if bfs_visited[i] == 0:
                queue.append(i)
                bfs_visited[i] = 1
                bfs_index.append(i)
    return bfs_index


graph = dict()

for i in range(m):
    s,e = map(int,input().split())
    if s in graph:
        graph[s].append(e)
    else:
        graph[s] = [e]
    if e in graph:
        graph[e].append(s)
    else:
        graph[e] = [s]

for i in graph.keys():
    graph[i] = sorted(graph[i])

result_dfs = dfs(n, graph, v)
for num in result_dfs:
    print(num, end= ' ')
print()
result_bfs = bfs(n, graph, v)
for num2 in result_bfs:
    print(num2, end= ' ')