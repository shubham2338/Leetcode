# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for i in lists:
            while i:
                arr.append(i.val)
                i=i.next
        arr.sort()
        h=ListNode(None)
        d=h
        for i in arr:
            f=ListNode(i)
            d.next=f
            d=d.next
            
        return h.next
            
        