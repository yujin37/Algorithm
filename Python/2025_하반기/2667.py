import sys
from collections import deque
input = sys.stdin.readline

town = list()
n = int(input())
for i in range(n):
    input_data = input().strip()
    town.append([int(ch) for ch in input_data])

def bfs(start_h, start_w):
    house = 1
    queue = deque([[start_h, start_w]])
    
    while queue:
        target = queue.popleft()
        town[target[0]][target[1]] = 0
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for m in range(4):
            if 0<= target[0]+dx[m] < n and 0<= target[1]+dy[m]<n:
                if town[target[0] + dx[m]][target[1]+dy[m]] == 1:
                    #타운 처리
                    queue.append([target[0] + dx[m], target[1] + dy[m]])
                    town[target[0] + dx[m]][target[1]+dy[m]] = 0 
                    house += 1
    return house
house_cnt = []
town_cnt = 0
for j in range(n):
    for k in range(n):
        if town[j][k] == 1:
            result = bfs(j, k)
            house_cnt.append(result)
            town_cnt += 1
print(town_cnt)
sorted_house_cnt = sorted(house_cnt)
for i in range(town_cnt):
    print(sorted_house_cnt[i])