# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(arr: ListNode) : #문자열 리스트노드 뒤집기 함수
            node, prev = arr, None

            while node:
                next, node.next = node.next, prev
                prev, node = node, next
            return prev
        
        def make_num(arr: ListNode): #리스트노드 문자열 바꾸어서 합치는 함수
            num = ''
            
            while arr:
                num += str(arr.val)
                arr = arr.next
            return num
        
        #리스트 노드 각각 뒤집기
        l1_reverse = reverse(l1)
        l2_reverse = reverse(l2)

        #합을 구해서 문자열로 다시 변환
        result = str(int(make_num(l1_reverse)) + int(make_num(l2_reverse)))
        
        #다시 구한 값을 리스트 노드로 변환
        head = ListNode(0)

        curr_node = head

        for i in range(len(result)):
            curr_node.next = ListNode(result[i])
            curr_node = curr_node.next
        
        # 뒤집기 함수 호출해서 다시 처리
        return reverse(head.next)

        