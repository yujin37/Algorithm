import sys
input = sys.stdin.readline

def repaint_chess(eight_board, start):
    cnt = 0
    
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                expect = start
            else:
                if start == 'W':
                    expect = 'B'
                else:
                    expect = 'W'
            if eight_board[i][j] != expect:
                cnt += 1
    return cnt
            
N, M = map(int,input().split())
board = []
for i in range(N):
    line = list(input())
    board.append(line)
if N == 8 and M == 8:
    result1 = repaint_chess(board, 'W')
    result2 = repaint_chess(board, 'B')
    print(min(result1, result2))
else:
    final_result = 64
    for i in range(N-7):
        for j in range(M-7):
            find_board = [row[j:j+8] for row in board[i:i+8]]
            result1 = repaint_chess(find_board, 'W')
            result2 = repaint_chess(find_board, 'B')
            final_result = min(final_result, result1, result2)
    print(final_result)