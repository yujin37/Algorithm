n=int(input())
cnt=0
result=list()
def move(n,start, end):
    global cnt
    result.append([start, end])
    cnt+=1
def hanoi(n, start, end, sub):
    global cnt
    if n==1:
        move(1,start, end)
        return
    else:
        hanoi(n-1, start, sub, end)
        move(n, start, end)
        hanoi(n-1, sub, end, start)
hanoi(n,1, 3, 2)
print(cnt)
for i in range(cnt):
    print(result[i][0], result[i][1])