# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = list()
        level = 0
        res = []

        if root:
            q.append(root)
        
        while q:
            res.append([])
            level_len = len(q)
            for _ in range(level_len):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                res[level].append(node.val)
            level += 1

        return [level[-1] for level in res]