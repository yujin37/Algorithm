#연습문제level 2
def solution(s):
    answer = ''
    s_list=list(s.split(' '))
    s_list=list(map(int, s_list))
    #print(min(s_list))
    answer=str(min(s_list))+' '+str(max(s_list))
    #print(answer)
    return answer
