n,m=map(int,input().split())
baguni=[0]*(n+1)
for t in range(m):
    i,j,k=map(int,input().split())
    for s in range(i,j+1):
        baguni[s]=k
for u in range(1,n+1):
    print(baguni[u], end=' ')