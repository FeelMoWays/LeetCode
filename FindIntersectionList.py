from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer1 = headA
        pointer2 = headB
        while pointer1 and pointer2:
            pointer1 = pointer1.next 
            pointer2 = pointer2.next
            if pointer1 == pointer2:
                return pointer1.val or pointer2.val
        return 0      