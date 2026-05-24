"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return
        node_map = {}
        visited = set()

        q = deque()
        q.append(node)

        while q:
            curr = q.popleft()
            visited.add(curr)
            if not curr.val in node_map:
                node_map[curr.val] = Node(curr.val)
            for neighbor in curr.neighbors:
                if not neighbor.val in node_map:
                    node_map[neighbor.val] = Node(neighbor.val)
                node_map[curr.val].neighbors.append(node_map[neighbor.val])
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return node_map[1]