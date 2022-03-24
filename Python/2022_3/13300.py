#방배정
#이 문제를 풀 때 주의해야 하는 것은 2차원 배열이다. c, c++과 달리 배열 위치는 서로 반대가 되어야 함
n,k=map(int,input().split())
std=[[0]*2 for _ in range(6)]
room=0
for _ in range(n):
    s,y=map(int,input().split())
    std[y-1][s-1]+=1
for i in range(2):
    for j in range(6):
        room+=(std[j][i]//k)
        if(std[j][i]%k>0):
            room+=1
print(room)
