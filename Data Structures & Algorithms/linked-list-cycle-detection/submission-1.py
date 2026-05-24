# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next == None:
            return False
        fast = slow = head
        while fast != None:
            if fast.next:
                fast = fast.next.next
            else: 
                fast = fast.next

            slow = slow.next
            if fast == slow:
                return True
        return False