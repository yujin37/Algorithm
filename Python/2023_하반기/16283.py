a, b, n, w= map(int,input().split())

s = 1
e = n - 1
result = []
for i in range(n-1):
    if a * s + b * e == w:
        result.append([s,e])

    s += 1
    e -= 1

if len(result) == 1:
    print(result[0][0], result[0][1])
else:
    print(-1)