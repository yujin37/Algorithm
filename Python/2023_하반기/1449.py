n, l = map(int,input().split())
tape = list(map(int,input().split()))
tape.sort()
start = tape[0] #처음 위치 기록하고
cnt = 1
for i in tape[1:]: #1부터 탐색하는데
    if i in range(start, start+l): #시작위치부터 테이프 범위에 있으면
        continue
    else:
        cnt +=1 #새로운 테이프
        start = i #위치 기록
print(cnt)