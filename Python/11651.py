#좌표정렬하기2
import sys
n=int(sys.stdin.readline())#속도를 빠르게 하기 위한 input
xy=[[]*2]*n#2차원 배열을 위한 작업
for i in range(n):
    xy[i]=list(map(int,sys.stdin.readline().split()))
xy.sort(key=lambda x:(x[1],x[0]))#뒤에 값을 기준으로 하되 만약 같다면 앞의 값으로 정렬
#위와 같지 않고 만약 for문으로 해결한다면 시간 초과가 남
for x,y in xy:
    print(x,y)
