# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result

        while list1 and list2:
            
            if list1.val <= list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next
        while list1 is not None:
            current.next = ListNode(list1.val)
            list1 = list1.next
            current = current.next
        while list2 is not None:
            current.next = ListNode(list2.val)
            list2 = list2.next
            current = current.next
       
        return result.next
        
