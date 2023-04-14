# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h=[]
        t=head
        while t is not None:
            h.append(t.val)
            t=t.next
        h.sort()
        d=ListNode()
        s=d
        for i in h:
            f=ListNode(i)
            d.next=f
            d=d.next
        return s.next