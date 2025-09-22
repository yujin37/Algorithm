import sys
input = sys.stdin.readline

def search_number(key, a, left, right):
    
    while left <= right:
        mid = (left+right)//2
        if key == a[mid]:
            return True
        elif key < a[mid]:
            right = mid-1
        else:
            left = mid+1
    return False            
n = int(input())
A = list(map(int,input().split()))

M = int(input())
B = list(map(int,input().split()))

A.sort()
for num in B:
    #탐색 알고리즘 호출하기
    if search_number(num, A, 0, n-1):
        print(1)
    else:
        print(0)