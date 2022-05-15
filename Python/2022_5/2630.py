#실버3, 색종이 만들기
import sys
num=int(sys.stdin.readline())
paper=[list(map(int,sys.stdin.readline().split())) for _ in range(num)]

w=0
b=0

def cut(x,y,num):
    global b,w
    check=paper[x][y]
    for i in range(x,x+num):
        for j in range(y,y+num):
            if check!=paper[i][j]:
                cut(x,y,num//2)
                cut(x,y+num//2,num//2)
                cut(x+num//2,y,num//2)
                cut(x+num//2, y+num//2, num//2)
                return
    if check==0:
        w+=1
        return
    else:
        b+=1
        return
cut(0,0,num)
print(w)
print(b)
