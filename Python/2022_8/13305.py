#실버4 주유소
import sys
input=sys.stdin.readline

n=int(input())
road=list(map(int,input().split())) #이건 각 도로간의 길이
pay=list(map(int,input().split())) #이건 각 지점에서 지불해야할 기름 값

money=0 #일단 총 계산해주는 곳
now=pay[0] #여긴 앞에서부터 싼 곳을 기록
for i in range(n-1):
    if pay[i]<now: #그래서 이전 것보다 현재 지불하는 것이 작다면
        now=pay[i] #지불해야 할 돈을 바꾸어주는데
    money+=now*road[i] #그렇지 않다면 그대로 갈 거고 아니면 바꾸어서 현재 위치에 대한 기름값을 지불한다.
print(money)
