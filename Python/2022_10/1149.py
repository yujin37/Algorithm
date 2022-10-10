#실버1, RGB 거리, DP 연습
n=int(input())
color=[]
for i in range(n):
    color.append(list(map(int,input().split()))) #일단 색깔을 입력받아 리스트 형태로 저장한다.
for i in range(1,len(color)): #1부터는 앞에것을 비교한다.
    color[i][0]+=min(color[i-1][1], color[i-1][2]) #빨간색과 이전 초록색, 파란색 중 최소를 더해서 넣어준다.
    color[i][1]+=min(color[i-1][0], color[i-1][2]) #여기도 마찬가지
    color[i][2]+=min(color[i-1][0], color[i-1][1])
print(min(color[n-1][0], color[n-1][1], color[n-1][2])) #이렇게 누적시킨 값 중 작은 것을 출력한다.
    
