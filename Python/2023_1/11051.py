def recursion(n1,k1):
    arr=[[0 for _ in range(k1+1)] for _ in range(n1+1)]
    for i in range(n1+1):
        for j in range(min(n1,k1)+1):
            if j==0 or j==i:
                arr[i][j]=1
            else:
                arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
    return arr[n1][k1]

n,k=map(int,input().split())
print(int(recursion(n,k)%10007))
