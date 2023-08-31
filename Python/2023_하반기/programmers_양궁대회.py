from itertools import combinations_with_replacement
def solution(n, info):
    answer = [-1]
    score = [0,1,2,3,4,5,6,7,8,9,10]
    max_gap = -1
    for i in list(combinations_with_replacement(score, n)):
        score_board = [0 for _ in range(11)]
        lion= 0
        apeach = 0
        for j in i:
            score_board[10-j] += 1
        #print(score_board)

        for k in range(11):
            if info[k] == score_board[k] ==0:
                continue
            
            elif info[k] >= score_board[k]:
                apeach += 10-k
            else:
                lion += 10-k
        if apeach >= lion:
            pass
            #print('apeach 승')
        else:
            #print('lion 승', lion)
            gap = lion - apeach
            if gap > max_gap:
                max_gap = gap
                answer = score_board
    #print(answer)
    return answer
    #return 'ㄴㄴㄴ'
n=5
info=[2,1,1,1,0,0,0,0,0,0,0]
print(solution(n,info)) #[0,2,2,0,1,0,0,0,0,0,0]
print('-----') 
n=1
info=[1,0,0,0,0,0,0,0,0,0,0]
print(solution(n,info)) #[-1]
print('-----')
n=9
info=[0,0,1,2,0,1,1,1,1,1,1] 
print(solution(n,info)) #[1,1,2,0,1,2,2,0,0,0,0]
print('-----')
n=10
info=[0,0,0,0,0,0,0,0,3,4,3]
print(solution(n,info)) #[1,1,1,1,1,1,1,1,0,0,2]