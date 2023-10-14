n, m, k = map(int,input().split())
tile = []
#타일 배열 추가
for i in range(n):
    tile.append(list(input()))
#print(tile)
result = 0
per_tile = (n*m) // (k*k)
result_tile = list()
for x in range(k):
    for y in range(k):
        count_list = [0] * 26
        for i in range(0,n-k+1, k):
            for j in range(0,m-k+1, k):
                count_list[ord(tile[i+x][j+y])-65] += 1
        max_alpha = chr(count_list.index(max(count_list))+ 65)
        for i in range(0,n-k+1, k):
            for j in range(0,m-k+1, k):
                if tile[i+x][j+y] != max_alpha:
                    tile[i+x][j+y] = max_alpha
        result += per_tile - max(count_list)
print(result)
for i in range(n):
    for j in range(m):
        print(tile[i][j], end='')
    print()