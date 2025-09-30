import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = dict()
for i in range(m):
    u, v = map(int,input().split())
    if u in graph.keys():
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph.keys():
        graph[v].append(u)
    else:
        graph[v] = [u]

def connected(status, start):
    global graph
    status[start] = 1
    if not start in graph.keys():
        return status
    for num in graph[start]:
        if status[num] == 0:
            connected(status, num)
    return status
visited = [0 for _ in range(n+1)]
cc = 0
for j in range(1,n+1):
    #방문하지 않았다면
    if visited[j] == 0:
        #방문 기록지랑 시작점
        visited = connected(visited, j)
        #호출할 때 연결 요소 개수 올려준다. 
        cc += 1

print(cc)