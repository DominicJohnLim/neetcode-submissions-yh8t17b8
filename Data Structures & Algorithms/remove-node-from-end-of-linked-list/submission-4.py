import copy
from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = 0
        triple = deque()
        return_head = head

        while head:
            current += 1
            triple.append(head)
            if current - n > 1:
                triple.popleft()
            head = head.next

        if len(triple) == 1:
            return 
        elif len(triple) == 2:
            # print(triple[0].val, triple[1].val)
            if n == 2:
                first = triple.popleft()
                second = triple.popleft()
                first.val = second.val
                first.next = None
                # print(first.val)
                return return_head
            else:
                # print("asdasd")
                first = triple.popleft()
                first.next = None
                return return_head
        else:
            m = len(triple)
            first = triple.popleft()
            second = triple.popleft()
            third = triple.popleft()
            if m == current and n == current:
                first.val = second.val
            first.next = third

            # print(first.val, first.next.val)
            return return_head
