from collections import deque
n=int(input())
circle=[i+1 for i in range(n)]
hnoi_emp=[]
hnoi=[]
hnoi.append(circle)
hnoi.append(hnoi_emp)
hnoi.append(hnoi_emp)
while True:
    cnt=0
    for i in range(1,n):
        if hnoi[2][i-1]<hnoi[2][i]:
            cnt+=1
        else:
            break
    if cnt+1 == n:
        break

#print(k)