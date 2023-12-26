import sys
input = sys.stdin.readline
arr = list()
def solve(n,m):
    for i in range(0, n-1):
        if arr[i+1][0] - arr[i][0] - arr[i][1] >= m: #다음 위치에서 앞의 위치 빼서 남으면
            return arr[i][0] + arr[i][1]  #그 위치로 출력
def solve2(n,m):
    if arr[-1][0] + arr[-1][1] + m <= s: #이건 마지막 위치 기록하고 소요시간을 더해 전체 시간 안넘으면
        return arr[-1][0] + arr[-1][1] # 그 위치를 출력한다.
def solution(n,m,s):
    for i in range(n):
        start, end = map(int,input().split())
        arr.append([start,end])
    arr.sort()
    
    if arr[0][0] >= m: #맨 처음에 m 만큼의 시간이 확보 되면
        print(0) #처음에 보여주면 됨
    elif solve(n,m) != None: #중간 삽입
        print(solve(n,m))
    elif solve2(n,m) != None: #마지막 삽입
        print(solve2(n,m))
    else:
        print(-1)
n,m,s = map(int,input().split())
solution(n,m,s)
