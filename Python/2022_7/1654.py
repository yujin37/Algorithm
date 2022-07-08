#실버2 랜선자르기
import sys
input=sys.stdin.readline

line=[]
k,n=map(int,input().split())
for i in range(k):#입력 받기
    h=int(input())
    line.append(h)


lan=max(line)#제일 큰수 뽑기, 이건 필수 x
#print(lan)
start,end=1,lan#처음과 끝점을 설정, 매번 할 필요 없음
while start<=end:#하나씩 올라가면서 하는게 맞음
    m=(start+end)//2#이건 이분 탐색이라서
    cnt=0
    for i in line:
        cnt+=(i//m)
    if cnt>=n:
        start=m+1#이제 개수가 많으면 나누는 수가 커져야 하므로
    else:
        end=m-1#개수가 적으면 나누는 수가 작아져야 함
print(end)#그리고 가장 큰 수 구하라고 했으므로 최종 end를 구하는게 맞음.
