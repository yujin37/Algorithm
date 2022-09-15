def solution(s):
    s_counter=s.lower()
    p_cnt=0
    y_cnt=0
    for i in s_counter:
        if i=='p':
            p_cnt+=1
        elif i=='y':
            y_cnt+=1
    if p_cnt==y_cnt:
        return True
    else:
        return False
