import sys
input = sys.stdin.readline  
n, k = map(int,input().split())

alpha = [False for _ in range(26)]
words = [input().rstrip() for _ in range(n)]
result = 0
def check():
    cnt = 0
    for word in words:#단어 방문 체크하는데
        flag = True
        for s in word: #해당 문자가
            if not alpha[ord(s)-97] : #방문한 적 없으면
                flag = False #불가라고 기록하고
                break #브레이크
        if flag: #방문한 적있으면
            cnt += 1 #단어 방문 가능으로 체크
    return cnt #결과 값 보내고
def dfs(start, depth):
    global result
    if depth == k: #깊이가 같아지면
        result = max(result, check()) #최종 결과값 도출하고
        return 
    for i in range(start, 26): #시작점 부터 탐색하는데
        if not alpha[i]: #만약 방문한 적 없으면
            alpha[i] = True #방문기록 하고
            dfs(i,depth+1) #다음 문자 탐색하고
            alpha[i] = False #다시 초기화
def teach(n,k):
    if k<5:#기준 길이보다 적으면 0
        return 0
    elif k==26: #모든 알파벳
        return n
    else:
        for char in ['a','c','i','n','t']: #만약 이 범위에 있으면
            alpha[ord(char) - ord('a')] = True #그 값을 true로 바꾸고 시작
        dfs(0,5)
        return result
print(teach(n,k))