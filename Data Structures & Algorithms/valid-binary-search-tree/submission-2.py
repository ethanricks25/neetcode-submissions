# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, bounds):
            if not node:
               return True
            if node.left and node.val <= node.left.val:
                return False
            if node.left and node.left.val <= bounds[0]:
                return False
            if node.right and node.val >= node.right.val:
                return False
            if node.right and node.right.val >= bounds[1]:
                return False
            return dfs(node.left, (bounds[0], node.val)) and dfs(node.right, (node.val, bounds[1]))
        return dfs(root, (-1001, 1001))
