from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        visited = set()
        graph = [[] for i in range(n)]
        q = deque()

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        q.append((0, -1))
    
        while q:
            node = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node[0]]:
                if neighbor == node[1]:
                    continue
                q.append((neighbor, node[0]))
        return len(visited) == n