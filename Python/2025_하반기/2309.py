import sys
input = sys.stdin.readline

def find_seven(h):
    nine_sum = sum(h)
    for i in range(8):
        for j in range(1,9):
            if nine_sum - (h[i] + h[j]) == 100:
                return [h[i], h[j]]
height = list()
for i in range(9):
    height.append(int(input()))
sorted_height = sorted(height)
fake_height = find_seven(height)

for i in range(9):
    if sorted_height[i] in fake_height:
        pass
    else:
        print(sorted_height[i])
print('-------')
from itertools import combinations
import sys
input = sys.stdin.readline

nine_heights = list()
for i in range(9):
    nine_heights.append(int(input()))
sorted_height = sorted(nine_heights)
find_aval = list(combinations(sorted_height, 2))

total = sum(sorted_height)
for i in range(len(find_aval)):
    if total - sum(find_aval[i]) == 100:
        sorted_height.remove(find_aval[i][0])
        sorted_height.remove(find_aval[i][1])
        break
for i in range(7):
    print(sorted_height[i])