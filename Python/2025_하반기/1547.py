M = int(input())
cups = [1, 2, 3]
for i in range(M):
    x, y = map(int,input().split())
    x_loc = cups.index(x) #x의 컴위치
    y_loc = cups.index(y) #y의 컵위치
    #찾은 위치에 서로 반대 값을 넣는다. 
    cups[y_loc] = x 
    cups[x_loc] = y 
print(cups[0])