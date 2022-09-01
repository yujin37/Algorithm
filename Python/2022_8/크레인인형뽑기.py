def solution(board, moves):
    bag=[]
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                if bag and board[j][i-1]==bag[-1]:
                    #bag.append(board[j][i-1])
                    bag.pop()
                    answer+=2
                else:
                    bag.append(board[j][i-1])
                board[j][i-1]=0
                    #print(bag)
                break
    return answer
