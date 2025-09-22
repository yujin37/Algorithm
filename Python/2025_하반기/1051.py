import sys
input = sys.stdin.readline
n, m = map(int,input().split())
board = []
for i in range(n):
    line = list(input().strip())
    board.append(line)


#입력 처리
max_size = min(n,m)

result=1
for i in range(1,max_size+1):
    for j in range(n):
        for k in range(m):

            if j+i < n and k+i < m:
                top_left, top_right = board[j][k], board[j][k+i]
                bottom_left, bottom_right = board[j+i][k], board[j+i][k+i]
                
                #같은지 확인 진행
                if top_left == top_right == bottom_left == bottom_right:
                    result = max((i+1)*(i+1), result)
print(result)