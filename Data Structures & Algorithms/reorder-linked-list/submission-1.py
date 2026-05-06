# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fp, sp = head, head
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
        mid = sp.next
        sp.next = None
        # reverse
        prev, cur = None, mid
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        lp, rp = head, prev
        while rp:
            tmp = lp.next
            tmp2 = rp.next
            lp.next = rp
            rp.next = tmp
            lp = tmp
            rp = tmp2
        


        
