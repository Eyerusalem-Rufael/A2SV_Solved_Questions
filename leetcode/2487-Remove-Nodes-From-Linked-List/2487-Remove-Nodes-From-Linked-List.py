# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        curr = head
        while curr:
            while stk and stk[-1].val < curr.val:
                stk.pop()
            stk.append(curr)
            curr = curr.next
            
        next = None
        while stk:
            curr = stk.pop()
            curr.next = next
            next = curr
        return curr