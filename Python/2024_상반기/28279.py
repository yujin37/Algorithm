from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

nums = deque()
for i in range(n):
    msg = input()
    if msg[0] == '1':
        msg_split = msg.split()
        nums.appendleft(msg_split[-1])
    elif msg[0] == '2':
        msg_split = msg.split()
        nums.append(msg_split[-1])

    elif msg[0] == '3':
        if nums:
            print(nums.popleft())
            #print(nums[0])
        else:
            print(-1)
    elif msg[0] == '4':
        if nums:
            print(nums.pop())
            #print(nums[0])
        else:
            print(-1)
    elif msg[0] == '5':
        print(len(nums))

    elif msg[0] == '6':
        if nums:
            print(0)
        else:
            print(1)
    
    elif msg[0] == '7':
        if nums:
            print(nums[0])
        else:
            print(-1)
    elif msg[0] == '8':
        if nums:
            print(nums[-1])
        else:
            print(-1)

    