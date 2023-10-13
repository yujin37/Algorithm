import sys
input = sys.stdin.readline
s = input().rstrip()
n = int(input())
arr = [[0] * 26]
arr[0][ord(s[0])-97] = 1
for i in range(1,len(s)):
    arr.append(arr[-1][:])
    arr[i][ord(s[i])-97]+= 1

for i in range(n):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    if l == 0:
        print(arr[r][ord(alpha)-97])
    else:
        print(arr[r][ord(alpha)-97]- arr[l-1][ord(alpha)-97])