import sys
from collections import deque
input = sys.stdin.readline

def split_case(num):
    minus = num - 1
    plus = num + 1
    multi = num * 2
    return [minus, plus, multi]

n, k = map(int,input().split())
graph = dict()

visited = [False] * 100001
def bfs(start):
    queue = deque()
    queue.append((start,0))
    visited[start] = True
    while queue:
        #print(graph)
        now, time = queue.popleft()
        if now == k:
            break
        if not now in graph.keys():
            graph[now] = split_case(now)
        for num in graph[now]:
            if 0<=num<= 100000 and not visited[num]:
                visited[num] = True
                queue.append((num, time+1))
    return time
result = bfs(n)
print(result)