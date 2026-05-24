# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rec(total_sum: int, power: int, l ):
            if not l:
                return total_sum
            node_value = l.val * 10 ** power
            return rec(total_sum + node_value, power + 1, l.next)
        total = rec(rec(0,0,l1), 0, l2)
        head = node = ListNode()
        for i in range(len(str(total))):
            node.val = int(str(total)[-1 - i])
            node.next = ListNode() if i < len(str(total)) - 1 else None
            node = node.next
        return head
