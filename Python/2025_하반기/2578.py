def row_bingo(board, now):
    if board[now].count(0) == 5:
        return True
def col_bingo(board, now):
    if board[0][now] == board[1][now] == board[2][now] == board[3][now] == board[4][now] == 0:
        return True
def dia_down_bingo(board):
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == 0:
        return True
def dia_up_bingo(board): 
    if board[4][0] == board[3][1] == board[2][2] == board[1][3] == board[0][4] == 0:
        return True
def check_bingo(board):
    cnt = 0
    for i in range(5):
        #가로 빙고
        if row_bingo(board, i): #가로줄 확인
            cnt += 1
    for i in range(5):
        #세로 빙고
        if col_bingo(board, i):  #세로줄 확인
            cnt += 1
    #대각선 확인
    if dia_down_bingo(board):
        cnt += 1
    if dia_up_bingo(board):
        cnt += 1
    return cnt

board = list()    
for i in range(5):
    line = list(map(int,input().split()))
    board.append(line)
called = list()
for i in range(5):
    line2 = map(int,input().split())
    called.extend(line2)


for i in range(25):
    #인덱스 검색
    
    for k in range(5):
        for j in range(5):
            if called[i] == board[k][j]:
                board[k][j] = 0
                break
    result = check_bingo(board)
    if result >= 3:
        print(i+1)
        break
        
    