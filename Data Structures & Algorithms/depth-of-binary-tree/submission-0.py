# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def rec(count, node):
            if not node:
                return count
            return max(rec(count + 1, node.left), rec(count+1, node.right))
        
        height = 0

        return rec(height, root)