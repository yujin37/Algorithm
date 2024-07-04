from itertools import *
import math

def check_number(number):
    if number == 1:
        return False
    for k in range(2, int(math.sqrt(number)+1)):
        if number % k == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    num_paper = list(numbers)
    paper = []
    #print(num_paper)
    for i in range(1,len(num_paper)+1):
        num_mix = list(permutations(num_paper, i))
        for j in range(len(num_mix)):
            numbers = int("".join(num_mix[j]))
            if numbers != 0 and numbers not in paper:
                paper.append(numbers)
       
    for num in paper:
        if check_number(num):
            answer += 1
            
    return answer

numbers = "011"
print(solution(numbers))