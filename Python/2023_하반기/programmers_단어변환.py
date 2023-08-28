from collections import deque


def solution(begin, target, words):
    answer = 0 #최소 변환 수
    q = deque()
    visited = [0 for _ in range(len(words))]
    q.append([begin, 0])
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        else:
            for i in range(len(words)):
                temp_cnt = 0
                if not visited[i]:
                    for j in range(len(word)):
                        if word[j] != words[i][j]:
                            temp_cnt += 1
                    if temp_cnt == 1:
                        q.append([words[i],cnt+1])
                        visited[i] = 1
    return answer
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
result = solution(begin, target, words)
print('결과',result)
print('--------------')
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
result = solution(begin, target, words)
print('결과',result)
