n = int(input())
w = list(map(int,input().split()))
w.sort()
start, end = 0, 2*n-1
result = float('inf')
for i in range(n):
    tmp = w[start] + w[end]
    #result.append(tmp)
    start+=1
    end -= 1
    if result > tmp:
        result = tmp
print(result)
