# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, sub):
            if not node and not sub:
                return True
            if node and sub and node.val == sub.val:
                return dfs(node.left, sub.left) and dfs(node.right, sub.right)
            else:
                return False
        if not root and subRoot:
            return False
        isSubtree = False
        if root.val == subRoot.val:
             isSubtree = dfs(root, subRoot)
        return True if isSubtree else self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)