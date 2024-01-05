import sys
input = sys.stdin.readline
n, m = map(int,input().split())

#표 만들기
tables = []
for i in range(n):
    table = list(map(int,input().split()))
    tables.append(table)
#print('처음 테이블')
#print(tables)

result_table = [[0] * n for _ in range(n)]
result_table[0][0] = tables[0][0]
for i in range(1,n):
    result_table[i][0] = result_table[i-1][0] + tables[i][0]
for i in range(1,n):
    result_table[0][i] = result_table[0][i-1] + tables[0][i]
    
for i in range(1, n):
    for j in range(1, n):
        result_table[i][j] = result_table[i-1][j] + result_table[i][j-1] - result_table[i-1][j-1]+ tables[i][j]

#print('현재 테이블')
#print(result_table)
#print('-----')
#구하고자 하는 곳
for j in range(m):
    #result = 0 #최종 값 저장
    x1,y1,x2,y2 = map(int,input().split())
    
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    
    result = result_table[x2][y2]
    
    if x1 > 0:
        result -= result_table[x1-1][y2]
    if y1 > 0:
        result -= result_table[x2][y1-1]
    if x1 > 0 and y1 > 0:
        result += result_table[x1-1][y1-1]
    
    print(result)
    
    