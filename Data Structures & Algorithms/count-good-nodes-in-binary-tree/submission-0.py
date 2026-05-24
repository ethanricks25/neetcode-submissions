# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = leftu
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val, count):
            if not node:
                return count
            if node.val >= max_val:
                count += 1
                max_val = node.val
            return dfs(node.left, max_val, count) + dfs(node.right, max_val, count) - count
        if not root:
            return 0
        return dfs(root, -999 , 0)