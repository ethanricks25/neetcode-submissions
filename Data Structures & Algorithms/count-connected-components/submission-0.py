class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        visited = set()
        components = 0
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                components += 1
        
        return components