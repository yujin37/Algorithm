n = int(input())
line = list(input())
m_cnt, w_cnt = 0, 0
result = 0
for i in range(len(line)):
    if abs(m_cnt - w_cnt) < n: #만약 차이가 n보다 작으면
        if line[i] == 'M': #남자이면 남자 증가
            m_cnt += 1
        else: #여자이면 여자 증가
            w_cnt += 1
        result += 1 #전체 개수 증가
    else: #만약 차이가 n보다 크면
        if line[i] == 'M': #만약 남자라면
            if abs(m_cnt+1 - w_cnt) < n: #만약 1개 더했을 때 차이가 범위라면
                m_cnt += 1
                result += 1
            else: #아니라면
                if i + 1 < len(line) and line[i+1] == 'W': #줄 안이면서 다음이 여자면
                    line[i], line[i+1] = line[i+1], line[i] #값을 바꿔주고
                    w_cnt += 1 #개수 올리고
                    result += 1 #총 개수 올린다.
                else: #그것도 아니면
                    break
        else:
            if abs(w_cnt+1 - m_cnt) < n: #만약 1개 더했을 때 차이가 범위라면
                w_cnt += 1
                result += 1
            else: #아니라면
                if i + 1 < len(line) and line[i+1] == 'M': #줄 안이면서 다음이 여자면
                    line[i], line[i+1] = line[i+1], line[i] #값을 바꿔주고
                    m_cnt += 1 #개수 올리고
                    result += 1 #총 개수 올린다.
                else: #그것도 아니면
                    break
print(result)