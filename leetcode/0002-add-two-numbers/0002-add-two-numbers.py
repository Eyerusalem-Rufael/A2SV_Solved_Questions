# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        curr = dummy_node
        first_digit = 0

        while l1 or l2 or first_digit:
            total = first_digit
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            last_digit = total % 10
            first_digit = total // 10
            curr.next = ListNode(last_digit)
            curr = curr.next

        return dummy_node.next