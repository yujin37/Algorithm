# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
from typing import List
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode()
        heap = []

        for i in range(len(lists)):
            if lists[i]: #일단 인덱스를 넣어서 처음값과 나머지 구조를 담아준다.
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        while heap:
            now = heapq.heappop(heap) #뽑아서
            idx = now[1] #현재 리스트에서의 몇번째 진행중인지 확인해주고
            result.next = now[2] #그리고 그다음 것을 설정해준다.

            result = result.next #그리고 현재라고 해놓고
            if result.next: #다음것이 있다면 다시 넣어준다.
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next #root는 처음에서 안움직였으므로 초기 상태로 된다. 