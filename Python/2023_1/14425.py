n,m = map(int,input().split())
setting=[]
cnt=0
for i in range(n):
    sen1=input()
    setting.append(sen1)
for i in range(m):
    sen2=input()
    if sen2 in setting:
        cnt+=1
print(cnt)