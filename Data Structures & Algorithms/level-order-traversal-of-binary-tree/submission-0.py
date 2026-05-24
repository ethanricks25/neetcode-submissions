# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = list()
        res = []
        level = 0
        if root:
            q.append(root)

        while q:
            level_length = len(q)
            res.append([])
            for _ in range(level_length):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                res[level].append(node.val)
            level += 1
        return res