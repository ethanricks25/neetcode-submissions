# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseGroup(head,k):
            prev = None
            nex = None
            node = head
            
            i = 0
            while node and i < k:
                i += 1
                node = node.next
            
            if i < k:
                return head, None
            
            i = 0

            while head and i < k:
                nex = head.next

                head.next = prev
                prev = head
                head = nex
                i += 1
            return prev,head
        
        prevForNextGroup = head
        endGroup, beginningOfNextGroup = reverseGroup(head,k)
        sol = endGroup
        
        while beginningOfNextGroup:
            tmp = beginningOfNextGroup
            endGroup, beginningOfNextGroup = reverseGroup(beginningOfNextGroup, k)
            prevForNextGroup.next = endGroup
            prevForNextGroup = tmp
        
        return sol