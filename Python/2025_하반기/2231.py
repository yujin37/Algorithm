import sys
input = sys.stdin.readline

def divide_sum(num):
    
    for i in range(1, num):
        split_num = list(map(int,str(i)))
        if sum(split_num) + i == num:
            return i
    return 0 
n = int(input())
print(divide_sum(n))