def music_playlist(n, satisfy):
    ldp = [0] * n
    maxldp = [0] * n
    rdp = [0] * n
    maxrdp = [0] * n

    #왼쪽 오른쪽 방향으로 dp 만들고 최댓값 만들어주는 리스트에 초기값 담기
    ldp[0] = satisfy[0] 
    maxldp[0] = ldp[0]
    rdp[n-1] = satisfy[n-1]
    maxrdp[n-1] = rdp[n-1]

    result = 0 #누적값 기록, 한번은 돌것이기 때문에
    for i in range(n):
        result+=satisfy[i]

    for t in range(1,n):
        ldp[t] = max(satisfy[t], ldp[t-1]+satisfy[t]) #왼쪽에 새롭게 담는게 나은지, 누적이 나은지 기록
        maxldp[t] = max(maxldp[t-1], ldp[t]) #최댓값이 갱신되는지 확인

    for t in range(n-2,-1,-1):
        rdp[t] = max(satisfy[t], rdp[t+1]+satisfy[t]) #오른쪽에 새롭게 담는게 나은지, 누적이 나은지 기록
        maxrdp[t] = max( maxrdp[t+1], rdp[t]) #최댓값이 갱신되는지 확인

    max_num = max(0, maxldp[n-1]) #처음부터 도는걸 기록, 0과 비교하는 이유는 작아지면 더해지지 않기 때문에
    for i in range(n-1):
        max_num = max(max_num, maxldp[i] + maxrdp[i+1]) #왼쪽 최대와 오른쪽 최대를 서로 비교
        #print(max_num)
    result += max_num #구해진 값을 최종 결과값에 넣음
    return result

n = int(input())
satisfy = list(map(int,input().split()))
print(music_playlist(n,satisfy))