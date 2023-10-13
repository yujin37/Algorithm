N, M = map(int,input().split())
A_matrix = list()
for i in range(N):
    line = list(map(int,input().split()))
    A_matrix.append(line)
M, K = map(int,input().split())
B_matrix = list()
for i in range(M):
    line = list(map(int,input().split()))
    B_matrix.append(line)
result_matrix = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            result_matrix[i][j] += A_matrix[i][k] * B_matrix[k][j]
for i in range(N):
    for j in range(K):
        print(result_matrix[i][j], end =' ')
    print()
    