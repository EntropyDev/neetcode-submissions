# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        
        lp = head
        for _ in range(n):
            lp = lp.next
        rp = dummy
        while lp:
            rp = rp.next
            lp = lp.next

        rp.next = rp.next.next

        return dummy.next