import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int,input().split())
site = defaultdict()
for i in range(n): #사이트 주소와 비밀번호가 주어진다.
    address, pw = input().rstrip().split()
    site[address] = pw
for j in range(m):
    find_value = input().rstrip()
    if site[find_value]:
        print(site[find_value])
    